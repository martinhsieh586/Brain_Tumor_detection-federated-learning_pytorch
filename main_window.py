# -*- coding: utf-8 -*-
from sklearn.metrics import accuracy_score

from Main_window.visualization_ui import *
from PyQt5.QtCore import QCoreApplication, QThread, pyqtSignal,QMutex
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPixmap
import cv2
import sys

sys.setrecursionlimit(1000000)
# federated function
from img_precess import *
from train import *
import server
from model import *

qmut_1=QMutex()
qmut_2=QMutex()
class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

# 執行緒1,處理模型訓練及聯邦學習操作
class Runthread(QThread):
    #  訓練參數顯示 - test 信號用法可刪除
    _signal = pyqtSignal(int)

    def __init__(self):
        super(Runthread, self).__init__()
        self.eval = server.server_eval()
    # pics_path: unlabel original img file
    def get_path(self, pics_path, pil_path, model, gpu_num, batch_size, epoch, exchange_epochs):
        # dict()
        self.pics_path = pics_path
        # dict()
        self.pil_path = pil_path
        # dict()
        self.model = model
        self.gpu_num=gpu_num
        self.batch_size=batch_size
        self.epoch=epoch
        self.exchange_epochs=exchange_epochs
        self.loss_func=nn.SmoothL1Loss()
        self.imge_size=tuple([80,80,1,4])
    def __del__(self):
        self.wait()

    def run(self):
        qmut_1.lock()

        self.acc = dict()
        self.pil_name = dict()
        train_img = dict()
        train_label = dict()
        # 訓練集影像預處理
        for i in self.model.keys():
            if self.pil_path[i] == '':
                self.pil_path[i] = None
            train_label[i], train_img[i] = envset(self.pil_path[i], self.pics_path[i], i)

        # 開始訓練
        print(f"train.....")
        print(f"epoch: {self.epoch}, batch_size: {self.batch_size}")
        if self.exchange_epochs > 0 and len(self.model) > 1:
            for exchange_epoch in range(self.exchange_epochs):
                for model_id in self.model.keys():
                    self.model[model_id]=train(model=self.model[model_id], loss_func=self.loss_func, train_loader=get_sample(train_label[model_id], train_img[model_id], int(self.batch_size)), epochs=self.epoch, image_size=self.imge_size)
                self.eval.exchange(self.model)
                print(f'exchange epoch: {exchange_epoch}, accuracy after federated learning: {self.eval.test(model=self.eval.server_model)}')
                self._signal.emit(exchange_epoch+1)
        else:
            for model_id in self.model.keys():
                self.model[model_id]=train(model=self.model[model_id], loss_func=self.loss_func, train_loader=get_sample(train_label[model_id], train_img[model_id], int(self.batch_size)), epochs=self.epoch, image_size=self.imge_size)
                # 評估模型準確率
                print(f'經過{self.epoch}次訓練後，準確率為:{int(self.eval.test(model=self.model[model_id])*100)}%')

        qmut_1.unlock()
        pass

# 執行緒2,圖片預測
class Runthread2(QThread):
    # 精準預測病種
    get_cls = pyqtSignal(int)

    def __init__(self):
        super(Runthread2,self).__init__()

    def get_paths(self, predict_pic_path, predict_model):
        self.predict_pic_path = predict_pic_path
        self.predict_model = predict_model
        self.imge_size = tuple([80,80,1,4])

    def run(self):
        qmut_2.lock()

        # 判斷病種準確率
        precise_actual = list()
        precise_pred = list()
        # 判斷是否罹癌準確率
        simple_actual = list()
        simple_pred = list()
        if not os.path.isfile(self.predict_pic_path):
            for i in os.listdir(self.predict_pic_path):
                img = self.predict_pic_path + i
                img_arr = Image_to_Tensor(img, self.imge_size[0], self.imge_size[1])
                prediction = self.predict_model.forward(img_arr)
                true_cls = self.predict_pic_path.split('/')[-2]
                print(f"影像 : {self.predict_pic_path + i}")
                print(f"Truth", end=' : ')
                self.get_cls.emit(int(true_cls))
                print(f"Prediction", end=' : ')
                self.get_cls.emit(np.argmax(prediction.clone().detach().numpy()))
                # 判斷病種準確率-紀錄
                precise_actual.append(int(true_cls))
                precise_pred.append(np.argmax(prediction.clone().detach().numpy()))
                # 判斷是否罹癌準確率-紀錄
                simple_actual.append(self.simple_cls(int(true_cls)))
                simple_pred.append(self.simple_cls(np.argmax(prediction.clone().detach().numpy())))
            precise_accuracy = accuracy_score(precise_actual, precise_pred)
            simple_accuracy = accuracy_score(simple_actual, simple_pred)
            print(f'判斷是否罹癌準確率 : {simple_accuracy*100}%')
            print(f'判斷腦癌病種準確率 : {precise_accuracy*100}%')

        if os.path.isfile(self.predict_pic_path):
            img_arr = Image_to_Tensor(self.predict_pic_path, self.imge_size[0], self.imge_size[1])
            prediction = self.predict_model.forward(img_arr)
            true_cls = self.predict_pic_path.split('/')[-2]
            print(f"影像 : {self.predict_pic_path}")
            print(f"Truth",end=' : ')
            self.get_cls.emit(int(true_cls))
            print(f"Prediction",end=' : ')
            self.get_cls.emit(np.argmax(prediction.clone().detach().numpy()))

        qmut_2.unlock()

    # 簡易判斷是否有罹癌
    def simple_cls(self, prediction):
        if prediction == 0:
            return 0
        elif 1 <= prediction <= 3:
            return 1


class MyWindow(QtWidgets.QMainWindow,Ui_MainWindowv):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setupUi(self)
        # self.set_second_ui(self)

        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stder = EmittingStream(textWritten=self.normalOutputWritten)


        # 參數初始化
        self.train_path = dict()
        self.pil_file_path = dict()
        self.exchange_model = dict()
        # 參與聯邦學習模型之計數器
        self.client_model_id = ''
        # ---------------------------------界面初始化——-------------------------------#
        # 設置窗口
        self.setWindowTitle("腦癌檢測")
        self.setWindowIcon(QIcon("ref_img/ntunhs_logo.png"))
        # 系統參數初始化
        self.sys_parameter_initialization()
        # 載入訓練集
        self.load_train_path.clicked.connect(self.load_train_pics)

        # 載入標註文件
        self.load_pil_path.clicked.connect(self.load_pil_file)

        # 輸出保存文件路徑
        self.pb_save_dir_path.clicked.connect(self.set_save_dir_path)
        ## 左側功能欄-button
        # 載入參與聯邦學習之模型
        self.exchange_model_input_path.clicked.connect(self.load_exchange_model)
        # 傳送本地端資訊給伺服器紀錄
        self.server_save.clicked.connect(self.client_2_server)
        # 重新設置參數
        self.pb_refresh.clicked.connect(self.refresh_parameters)
        # 運行訓練
        self.pb_run.clicked.connect(self._run)
        # 保存訓練好模型
        self.pb_save.clicked.connect(self.save_model)
        # 退出界面設置
        self.pb_quit.clicked.connect(self.set_quit)

        # 執行緒定義
        self.thread = None
        self.thread2 = None
        # 客戶端模型編號確認保存
        self.client_id_comfirm.clicked.connect(self.client_id_setting)
        # 辨識單張圖片
        self.recognit_pic.clicked.connect(self.recognite_pic_fun)
        # 辨識圖片集
        self.recognit_batch.clicked.connect(self.recognit_batch_fun)
        # 刷新
        self.refresh2.clicked.connect(self.refresh2_fun)
        # 載入辨識模型
        self.load_model.clicked.connect(self.load_model_fun)
        # 開始圖片辨識
        self.recognition.clicked.connect(self.recongnition_fun)

    # 載入訓練集路徑
    def load_train_pics(self):
        if self.client_model_id == '':
            QMessageBox.warning(self, "提示", "請輸入您的客戶端編號再載入訓練集")
            return
        self.text_load_train_path.clear()
        load_dir_path = QFileDialog.getExistingDirectory(self, "載入訓練集")
        if not os.path.exists(load_dir_path):
            QMessageBox.warning(self, "提示", "輸入文件目錄不存在，請重新選擇")
            return
        self.text_load_train_path.setText(load_dir_path+'/')

    # 選擇訓練好的標註圖檔集
    def load_pil_file(self):
        if self.client_model_id == '':
            QMessageBox.warning(self, "提示", "請輸入您的客戶端編號再載入標註圖檔集")
            return
        self.text_load_pil_path.clear()
        load_pil_path,_ = QFileDialog.getOpenFileName(self, "Open pil file for train", "C:",
                                                   "p(*.p)")
        # 如果用戶主動關閉文件對話框，則返回值為空
        if not os.path.exists(load_pil_path):  # 判斷路徑非空值
            QMessageBox.warning(self, "提示", "輸入文件目錄不存在，請重新選擇")
            return
        self.text_load_pil_path.setText(load_pil_path)

    # 設置模型保存路徑
    def set_save_dir_path(self):
        self.le_save_dir_path.clear()
        save_dir_path = QFileDialog.getExistingDirectory(self, "輸入模型保存路徑", self.output_save_path)
        if not os.path.exists(save_dir_path):
            QMessageBox.warning(self, "提示", "輸入模型保存路徑不存在，請重新選擇")
            return
        self.output_save_path = save_dir_path
        self.le_save_dir_path.setText(self.output_save_path)
        print("模型保存路徑:", self.output_save_path)
        pass

    # 載入參與聯邦學習模型
    def load_exchange_model(self):
        if self.client_model_id == '':
            QMessageBox.warning(self, "提示", "請輸入您的客戶端編號再載入模型")
            return
        self.text_exchange_model_input_path.clear()
        # 每添加一個檔案類型則需要加兩個分號
        model_dir, _ = QFileDialog.getOpenFileName(self, "Open pretrain model", "C:",
                                                   "pkl(*.pkl);;pt(*.pt);;dict(*.dict)")
        # 如果用戶主動關閉文件對話框，則返回值為空
        if not os.path.exists(model_dir):  # 判斷路徑非空值
            QMessageBox.warning(self, "提示", "載入模型路徑不存在，請重新選擇")
            return
        self.text_exchange_model_input_path.setText(model_dir)

    # 傳送本地端資訊給伺服器紀錄
    def client_2_server(self):
        # 訓練集目錄紀錄
        self.train_path[self.client_model_id] = self.text_load_train_path.text()
        # 已標註圖檔集路徑紀錄
        self.pil_file_path[self.client_model_id] = self.text_load_pil_path.text()
        # 載入模型紀錄
        if self.text_exchange_model_input_path.text() != '':
            self.exchange_model[self.client_model_id] = torch.load(self.text_exchange_model_input_path.text())
        elif self.checkBox_train_init.isChecked():
            self.exchange_model[self.client_model_id] = model_init()
        # 輸出文字介面清空
        self.te_screen_display.clear()
        # 輸入欄清空
        self.input_bar_initialization()
        print(f"目前載入客戶端編號: {self.client_model_id}")
        print(f"訓練集目錄: {self.train_path[self.client_model_id]}")
        print(f"已標註圖檔集:{self.pil_file_path[self.client_model_id]}")
        self.client_model_id = ''

    # 參數重新設置
    def refresh_parameters(self):
        # 輸出文字介面清空
        self.te_screen_display.clear()
        # 全部參數初始化
        self.sys_parameter_initialization()
        # 輸入欄清空
        self.input_bar_initialization()

    # 退出介面
    def set_quit(self):
        QCoreApplication.instance().quit()

    # 保存模型
    def save_model(self):
        save_dir_path = self.le_save_dir_path.text()

        if not os.path.exists(save_dir_path) or save_dir_path == '':
            save_dir_path = 'C:/Users/marti/Python_project/federated learning pytorch/QT_gui/fed_server_sim/model'
            if not os.path.exists(save_dir_path):
                os.makedirs(save_dir_path)
        # save model
        for i in self.exchange_model.keys():
            torch.save(self.thread.model[i], save_dir_path + "/" + i +'.pkl')
            print(f'編號: {i} 保存成功{save_dir_path + "/" + i +".pkl"}')

    # client model id setting
    def client_id_setting(self):
        self.client_model_id = self.client_id.text()

    # 開始訓練線程
    def _run(self):
        # 訓練參數設置
        batch_size = int(self.comboBox_2.currentText())
        epoch = int(self.comboBox.currentText())
        self.exchange_epochs = int(self.comboBox_3.currentText())
        # 進度條
        self.exchange_bar.setRange(0,self.exchange_epochs)
        # gpu
        if self.checkBox_gpu.isChecked():
            gpu_num=1
        else:
            gpu_num=0

        # for i in self.exchange_model.keys():
        #     print(f"參與載入客戶端編號: {i}")
        #     print(f"訓練集目錄: {self.train_path[i]}")
        #     print(f"已標註圖檔集:{self.pil_file_path[i]}")

        self.thread = Runthread()
        # pics_path: unlabel original img file
        self.thread.get_path(self.train_path, self.pil_file_path, self.exchange_model, gpu_num, batch_size, epoch, self.exchange_epochs)
        self.thread._signal.connect(self.exchange_bar_update)
        self.thread.start()
    # 更新進度條
    def exchange_bar_update(self, epochs):
        self.exchange_bar.setValue(epochs)

    # 載入單張預測圖片
    def recognite_pic_fun(self):
        self.recognit_pic_path.clear()

        recog_pic_path, dir_type = QFileDialog.getOpenFileNames(self, "選擇想辨識之圖片", "datasets")
        # 判斷文件路徑是否正確
        if len(recog_pic_path):
            for each_path in recog_pic_path:
                temp=each_path.split(".")[-1]
                if temp not in ["jpg","bmp","JPG","jpeg","BMP"] and not os.path.exists(each_path):
                    QMessageBox.warning(self, "提示", "文件路徑錯誤，請重新選擇!")
                    return

                self.rec_pic_path = recog_pic_path[0]
                self.recognit_pic_path.setText(self.rec_pic_path)
                print("預辨識圖片:", self.rec_pic_path)

                self.Show_image(self.rec_pic_path)
                return
        else:
            return
        pass

    # 載入圖片集做預測
    def recognit_batch_fun(self):
        self.recognit_batch_path.clear()
        load_image_path = QFileDialog.getExistingDirectory(self, "載入訓練集")
        # 如果用戶主動關閉文件對話框，則返回值為空
        if not os.path.exists(load_image_path):  # 判斷路徑非空值
            QMessageBox.warning(self, "提示", "輸入文件目錄不存在，請重新選擇")
            return
        self.recognit_batch_path.setText(load_image_path)
        print("圖片路徑:", load_image_path)

    # 載入預測模型
    def load_model_fun(self):
        self.load_model_path.clear()
        # 每添加一個檔案類型則需要加兩個分號
        model_dir, _ = QFileDialog.getOpenFileName(self, "Open pretrain model", "C:",
                                                   "pkl(*.pkl);;pt(*.pt);;dict(*.dict)")
        # 如果用戶主動關閉文件對話框，則返回值為空
        if not os.path.exists(model_dir):  # 判斷路徑非空值
            QMessageBox.warning(self, "提示", "載入模型路徑不存在，請重新選擇")
            return
        # 載入預測模型
        self.predict_model = torch.load(model_dir)
        self.load_model_path.setText(model_dir)

    # 清空右側辨識區
    def refresh2_fun(self):
        self.recognit_pic_path.clear()
        self.recognit_batch_path.clear()
        self.load_model_path.clear()
        self.label_img_show.clear()
        if self.predict_model != None:
            del self.predict_model

    # 辨識圖片
    def recongnition_fun(self):
        # 優先預測圖片集
        if self.recognit_batch_path.text() == '':
            predict_pic_path = self.recognit_pic_path.text()
        else:
            predict_pic_path = self.recognit_batch_path.text() + '/'

        # 辨識圖片線程
        self.thread2 = Runthread2()
        # pics_path: unlabel original img file
        self.thread2.get_paths(predict_pic_path, self.predict_model)
        self.thread2.get_cls.connect(self.pred_cls)

        self.thread2.start()

    # 類別名稱分類
    def pred_cls(self, prediction):
        if prediction == 0:
            print('normal')
        elif prediction == 1:
            print('meningioma_tumor')
        elif prediction == 2:
            print('glioma_tumor')
        elif prediction == 3:
            print('pituitary_tumor')

    def Show_image(self, outdir):
        image = QtGui.QPixmap(outdir).scaled(self.label_img_show.width(), self.label_img_show.height())
        self.label_img_show.setPixmap(image)
        pass

    # 參數初始化
    def sys_parameter_initialization(self):
        print("請開始訓練模型.........")
        self.output_save_path = ""
        if self.client_model_id != '':
            del self.train_path[self.client_model_id]
            del self.pil_file_path[self.client_model_id]
            del self.exchange_model[self.client_model_id]
        self.model_file_path = ""
        self.rec_pic_path = ""
        self.recongnit_batchs_path = ""
        self.model_path = ""
        self.class_path = ''

    # 輸入欄位清空
    def input_bar_initialization(self):
        # 文字欄位清空 - 左側功能
        self.client_id.setText('')
        self.recognit_pic_path.setText('')
        self.recognit_batch_path.setText('')
        self.load_model_path.setText('')
        self.text_load_train_path.setText('')
        self.text_load_pil_path.setText('')
        self.text_exchange_model_input_path.setText('')
        # 設置保存模型路徑
        self.le_save_dir_path.setText('')

    def normalOutputWritten(self, text):
        """Append text to the QTextEdit."""
        cursor = self.te_screen_display.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.te_screen_display.setTextCursor(cursor)
        self.te_screen_display.ensureCursorVisible()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
