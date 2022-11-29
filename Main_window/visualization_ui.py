# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualization_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator, QPixmap
from PyQt5.QtWidgets import QLabel


class Ui_MainWindowv(object):
    def setupUi(self, MainWindowv):
        MainWindowv.setObjectName("MainWindowv")
        MainWindowv.showFullScreen()
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setUnderline(False)
        MainWindowv.setFont(font)
        MainWindowv.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindowv.setAutoFillBackground(False)
        MainWindowv.setStyleSheet("background-color: rgb(221, 221, 221);\n"
"color: rgb(13, 13, 13);")
        MainWindowv.setAnimated(True)
        # 畫面上方
        self.centralwidget = QtWidgets.QWidget(MainWindowv)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        # 標題文字
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(16, 16, 16);")
        self.label.setLineWidth(2)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 2, 1, 1)

        # # 北護logo
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setAlignment(Qt.AlignLeft)
        jpg = QtGui.QPixmap("./ref_img/ntunhs_logo.png").scaled(self.label2.width()+150, self.label2.height()+20)
        self.label2.setPixmap(jpg)
        self.gridLayout_2.addWidget(self.label2, 0, 0, 1, 1)

        # 整體介面
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("background-color: rgb(211, 255, 224);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        # 上方logo
        self.titleAreaWidgetContents = QtWidgets.QWidget()
        self.titleAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 784, 297))
        self.titleAreaWidgetContents.setObjectName("titleAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.titleAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout_3")
        self.tabWidget_info_show = QtWidgets.QTabWidget(self.titleAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget_info_show.setFont(font)
        self.tabWidget_info_show.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget_info_show.setStyleSheet("background-color: rgb(124, 221, 215);font: 12pt \"Microsoft JhengHei\";")
        self.tabWidget_info_show.setObjectName("tabWidget_info_show")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")

        # 右側功能列
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 784, 297))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget_info_show = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget_info_show.setFont(font)
        self.tabWidget_info_show.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget_info_show.setStyleSheet("background-color: rgb(124, 221, 215);font: 12pt \"Microsoft JhengHei\";")
        self.tabWidget_info_show.setObjectName("tabWidget_info_show")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        # 上方預測後影像呈現物件
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        # 下方預測前參數設置
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        # 載入預測模型
        self.load_model = QtWidgets.QPushButton(self.tab_7)
        self.load_model.setStyleSheet("background-color: rgb(209, 209, 104);")
        self.load_model.setObjectName("load_model")
        self.gridLayout_6.addWidget(self.load_model, 0, 1, 1, 1)
        # 載入預測模型-欄位輸入
        self.load_model_path = QtWidgets.QLineEdit(self.tab_7)
        self.load_model_path.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.load_model_path.setObjectName("load_model_path")
        self.gridLayout_6.addWidget(self.load_model_path, 0, 3, 1, 1)
        # 測試圖片路徑
        self.recognit_pic = QtWidgets.QPushButton(self.tab_7)
        self.recognit_pic.setStyleSheet("background-color: rgb(209, 209, 104);")
        self.recognit_pic.setObjectName("recognit_pic")
        self.gridLayout_6.addWidget(self.recognit_pic, 1, 1, 1, 1)
        # 測試圖片路徑-欄位輸入
        self.recognit_pic_path = QtWidgets.QLineEdit(self.tab_7)
        self.recognit_pic_path.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.recognit_pic_path.setObjectName("recognit_pic_path")
        self.gridLayout_6.addWidget(self.recognit_pic_path, 1, 3, 1, 1)
        # 識別資料集路徑
        self.recognit_batch = QtWidgets.QPushButton(self.tab_7)
        self.recognit_batch.setStyleSheet("background-color: rgb(209, 209, 104);")
        self.recognit_batch.setObjectName("recognit_batch")
        self.gridLayout_6.addWidget(self.recognit_batch, 2, 1, 1, 1)
        # 識別資料集路徑-欄位輸入
        self.recognit_batch_path = QtWidgets.QLineEdit(self.tab_7)
        self.recognit_batch_path.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.recognit_batch_path.setObjectName("recognit_batch_path")
        self.gridLayout_6.addWidget(self.recognit_batch_path, 2, 3, 1, 1)
        # 圖片清空刷新
        self.refresh2 = QtWidgets.QPushButton(self.tab_7)
        self.refresh2.setStyleSheet("background-color: rgb(209, 209, 104);")
        self.refresh2.setObjectName("refresh2")
        self.gridLayout_6.addWidget(self.refresh2, 1, 4, 1, 1)
        # 識別
        self.recognition = QtWidgets.QPushButton(self.tab_7)
        self.recognition.setStyleSheet("background-color: rgb(209, 209, 104);")
        self.recognition.setObjectName("recognition")
        self.gridLayout_6.addWidget(self.recognition, 2, 4, 1, 1)
        # 預測後影像呈現
        self.gridLayout_5.addLayout(self.gridLayout_6, 4, 5, 1, 1)
        self.label_img_show = QtWidgets.QLabel(self.tab_7)
        self.label_img_show.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_img_show.setStyleSheet("background-color: rgb(255, 255, 255);border:2px solid blue;")
        self.label_img_show.setText("")
        self.label_img_show.setObjectName("label_img_show")
        self.gridLayout_5.addWidget(self.label_img_show, 2, 5, 2, 1)
        self.tabWidget_info_show.addTab(self.tab_7, "")
        self.gridLayout_3.addWidget(self.tabWidget_info_show, 2, 1, 1, 1)
        # 左側訓練畫面
        self.tabWidget_oper = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget_oper.setFont(font)
        self.tabWidget_oper.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget_oper.setStyleSheet("background-color: rgb(124, 221, 215);font: 12pt \"Microsoft JhengHei\";")
        self.tabWidget_oper.setObjectName("tabWidget_oper")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        # 下方輸出結果顯示窗
        self.te_screen_display = QtWidgets.QTextEdit(self.tab_6)
        self.te_screen_display.setStyleSheet("background-color: rgb(200, 200, 200);border:2px solid blue;")
        self.te_screen_display.setObjectName("te_screen_display")
        # 下方輸出結果顯示窗-位置
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.addWidget(self.te_screen_display, 4, 0, 1, 1)
        # 上方參數設置
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        # 保持欄寬放大後不變形
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        # 載入訓練集路徑
        self.load_train_path = QtWidgets.QPushButton(self.tab_6)
        self.load_train_path.setStyleSheet("background-color: rgb(175, 177, 255);")
        self.load_train_path.setObjectName("load_train_path")
        self.gridLayout.addWidget(self.load_train_path, 1, 0, 1, 1)
        # 保存訓練後模型路徑-輸入路徑欄
        self.text_load_train_path = QtWidgets.QLineEdit(self.tab_6)
        self.text_load_train_path.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.text_load_train_path.setObjectName("text_load_train_path")
        self.gridLayout.addWidget(self.text_load_train_path, 1, 1, 1, 1)
        # 載入已標註圖像檔
        self.load_pil_path = QtWidgets.QPushButton(self.tab_6)
        self.load_pil_path.setStyleSheet("background-color: rgb(175, 177, 255);")
        self.load_pil_path.setObjectName("load_pil_path")
        self.gridLayout.addWidget(self.load_pil_path, 2, 0, 1, 1)
        # 載入已標註圖像檔-輸入路徑欄
        self.text_load_pil_path = QtWidgets.QLineEdit(self.tab_6)
        self.text_load_pil_path.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.text_load_pil_path.setObjectName("text_load_pil_path")
        self.gridLayout.addWidget(self.text_load_pil_path, 2, 1, 1, 1)
        # 保存訓練後模型路徑
        self.pb_save_dir_path = QtWidgets.QPushButton(self.tab_6)
        self.pb_save_dir_path.setStyleSheet("background-color: rgb(175, 177, 255);")
        self.pb_save_dir_path.setObjectName("pb_save_dir_path")
        self.gridLayout.addWidget(self.pb_save_dir_path, 3, 0, 1, 1)
        # 保存訓練後模型路徑-輸入路徑欄
        self.le_save_dir_path = QtWidgets.QLineEdit(self.tab_6)
        self.le_save_dir_path.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.le_save_dir_path.setObjectName("le_save_dir_path")
        self.gridLayout.addWidget(self.le_save_dir_path, 3, 1, 1, 1)
        # 載入參與聯邦學習之客戶端預訓練模型路徑
        self.exchange_model_input_path = QtWidgets.QPushButton(self.tab_6)
        self.exchange_model_input_path.setStyleSheet("background-color: rgb(175, 177, 255);")
        self.exchange_model_input_path.setObjectName("exchange_model_input_path")
        self.gridLayout.addWidget(self.exchange_model_input_path, 4, 0, 1, 1)
        # 載入參與聯邦學習之客戶端預訓練模型路徑-輸入路徑欄
        self.text_exchange_model_input_path = QtWidgets.QLineEdit(self.tab_6)
        self.text_exchange_model_input_path.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.text_exchange_model_input_path.setObjectName("text_exchange_model_input_path")
        self.gridLayout.addWidget(self.text_exchange_model_input_path, 4, 1, 1, 1)
        # 傳送本地端資訊給伺服器端保存
        self.server_save = QtWidgets.QPushButton(self.tab_6)
        self.server_save.setStyleSheet("background-color: rgb(175, 177, 255);")
        self.server_save.setObjectName("server_save")
        self.gridLayout.addWidget(self.server_save, 5, 0, 1, 1)
        # 刷新
        self.pb_refresh = QtWidgets.QPushButton(self.tab_6)
        self.pb_refresh.setStyleSheet("background-color: rgb(175, 177, 255);")
        self.pb_refresh.setObjectName("pb_refresh")
        self.gridLayout.addWidget(self.pb_refresh, 5, 1, 1, 1)
        # 訓練
        self.pb_run = QtWidgets.QPushButton(self.tab_6)
        self.pb_run.setStyleSheet("background-color: rgb(175, 177, 255);")
        self.pb_run.setObjectName("pb_run")
        self.gridLayout.addWidget(self.pb_run, 5, 2, 1, 1)
        # 保存模型
        self.pb_save = QtWidgets.QPushButton(self.tab_6)
        self.pb_save.setStyleSheet("background-color: rgb(175, 177, 255);")
        self.pb_save.setObjectName("pb_save")
        self.gridLayout.addWidget(self.pb_save, 5, 3, 1, 1)
        # 退出
        self.pb_quit = QtWidgets.QPushButton(self.tab_6)
        self.pb_quit.setStyleSheet("background-color: rgb(175, 177, 255);")
        self.pb_quit.setObjectName("pb_quit")
        self.gridLayout.addWidget(self.pb_quit, 5, 4, 1, 1)
        # 客戶端模型編號輸入
        self.client_id = QtWidgets.QLineEdit(self.tab_6)
        # 限制只能輸入英文或數字
        self.pValidator = QRegExpValidator(self)
        reg=QRegExp('[a-zA-Z0-9]+$')
        self.pValidator.setRegExp(reg)
        self.client_id.setValidator(self.pValidator)
        self.client_id.setObjectName("client_id")
        self.client_id.setStyleSheet("background-color: rgb(100, 150, 100);")
        self.gridLayout.addWidget(self.client_id, 0, 1, 1, 3)
        # 確認客戶端模型編號按鈕
        self.client_id_comfirm = QtWidgets.QPushButton(self.tab_6)
        self.client_id_comfirm.setStyleSheet("background-color: rgb(175, 177, 255);")
        self.client_id_comfirm.setObjectName("client_id_comfirm")
        self.gridLayout.addWidget(self.client_id_comfirm, 0, 4, 1, 1)
        # 編號輸入文字顯示
        self.client_id_input = QLabel('客戶端模型編號輸入 : ')
        self.client_id_input.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.client_id_input, 0, 0, 1, 1)
        # train epoch 選擇:下拉框
        self.label_epoch = QtWidgets.QLabel(self.tab_6)
        self.label_epoch.setObjectName("label_epoch")
        self.gridLayout.addWidget(self.label_epoch, 2, 3, 1, 1)
        # batch size 選擇:下拉框
        self.label_batch = QtWidgets.QLabel(self.tab_6)
        self.label_batch.setObjectName("label_batch")
        self.gridLayout.addWidget(self.label_batch, 3, 3, 1, 1)
        # exchange epoch 選擇:下拉框
        self.label_exchange = QtWidgets.QLabel(self.tab_6)
        self.label_exchange.setObjectName("label_exchange")
        self.gridLayout.addWidget(self.label_exchange, 4, 3, 1, 1)
        # gpu 開啟
        self.checkBox_gpu = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_gpu.setObjectName("checkBox_gpu")
        self.gridLayout.addWidget(self.checkBox_gpu, 1, 3, 1, 1)
        # 初始化模型訓練 開啟
        self.checkBox_train_init = QtWidgets.QCheckBox(self.tab_6)
        self.checkBox_train_init.setObjectName("checkBox_train_init")
        self.gridLayout.addWidget(self.checkBox_train_init, 1, 4, 1, 1)
        # 下拉框 - train epochs set
        self.comboBox = QtWidgets.QComboBox(self.tab_6)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox") # 對象名稱，用css樣式
        # 下拉框个数，添加多少个数，就写多少个
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 4, 1, 1)
        # 下拉框 - batch size set
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        # 下拉框個數，依需求增加
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 3, 4, 1, 1)
        # 下拉框 - exchange epoch set
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        # 下拉框個數，依需求增加
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 4, 4, 1, 1)
        # 聯邦學習進度條顯示
        self.exchange_bar = QtWidgets.QProgressBar(self.tab_6)
        self.exchange_bar.setObjectName("exchange_bar")
        ## 進度條樣式
        self.exchange_bar.setStyleSheet('''
            QProgressBar {
                border: 2px solid #000;
                text-align:center;
                background:#aaa;
                color:#fff;
                height: 15px;
                border-radius: 8px;
                width:150px;
            }
            QProgressBar::chunk {
                background: #333;
                width:1px;
            }
        ''')
        self.gridLayout_exchange_bar = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_exchange_bar.setObjectName("gridLayout_exchange_bar")
        self.gridLayout_exchange_bar.addWidget(self.exchange_bar, 0, 1, 1, 1)
        # 聯邦學習進度條文字顯示
        self.exchange_bar_text = QLabel('當前聯邦學習進度 : ')
        self.exchange_bar_text.setAlignment(Qt.AlignCenter)
        self.gridLayout_exchange_bar.addWidget(self.exchange_bar_text, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_exchange_bar, 3, 0, 1, 1)

        # 將窗口布置呼叫並顯示於介面
        self.gridLayout_4.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.tabWidget_oper.addTab(self.tab_6, "")
        self.gridLayout_3.addWidget(self.tabWidget_oper, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 5)
        MainWindowv.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowv)
        self.tabWidget_info_show.setCurrentIndex(0)
        self.tabWidget_oper.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindowv)

    def retranslateUi(self, MainWindowv):
        _translate = QtCore.QCoreApplication.translate
        MainWindowv.setWindowTitle(_translate("MainWindowv", "MainWindow"))
        self.label.setText(_translate("MainWindowv", "聯邦學習-腦癌辨識系統"))
        # 預測評估-右側
        self.recognit_pic.setText(_translate("MainWindowv", "載入預辨識之圖片"))
        self.load_model.setText(_translate("MainWindowv", "載入預測模型"))
        self.recognit_batch.setText(_translate("MainWindowv", "批量識別"))
        self.refresh2.setText(_translate("MainWindowv", "刷新"))
        self.recognition.setText(_translate("MainWindowv", "識別"))
        self.tabWidget_info_show.setTabText(self.tabWidget_info_show.indexOf(self.tab_7), _translate("MainWindowv", "執行顯示"))
        # 預測評估-左側
        self.load_train_path.setText(_translate("MainWindowv", "1.載入訓練集"))
        self.load_pil_path.setText(_translate("MainWindowv", "2.載入已標註圖檔集"))
        self.pb_save_dir_path.setText(_translate("MainWindowv", "3.模型保存路徑"))
        self.exchange_model_input_path.setText(_translate("MainWindowv", "4.載入參與聯邦學習之模型"))
        self.server_save.setText(_translate("MainWindowv", "傳送本地端資訊給伺服器"))
        self.pb_refresh.setText(_translate("MainWindowv", "刷新"))
        self.pb_run.setText(_translate("MainWindowv", "訓練"))
        self.pb_save.setText(_translate("MainWindowv", "保存模型"))
        self.pb_quit.setText(_translate("MainWindowv", "退出"))
        self.checkBox_gpu.setText(_translate("MainWindowv", "gpu"))
        self.checkBox_train_init.setText(_translate("MainWindowv", "train init"))
        self.client_id_comfirm.setText(_translate("MainWindowv", "確認編號"))
        self.label_batch.setText(_translate("MainWindowv", "Batch_Size"))
        self.label_epoch.setText(_translate("MainWindowv", "Epoch"))
        self.label_exchange.setText(_translate("MainWindowv", "Exchange Epoch"))
        # 下拉式表單選項 : train epochs set
        self.comboBox.setItemText(0, _translate("MainWindowv", "10"))
        self.comboBox.setItemText(1, _translate("MainWindowv", "50"))
        self.comboBox.setItemText(2, _translate("MainWindowv", "100"))
        self.comboBox.setItemText(3, _translate("MainWindowv", "300"))
        self.comboBox.setItemText(4, _translate("MainWindowv", "500"))
        # 下拉式表單選項 : batch size set
        self.comboBox_2.setItemText(0, _translate("MainWindowv", "16"))
        self.comboBox_2.setItemText(1, _translate("MainWindowv", "32"))
        self.comboBox_2.setItemText(2, _translate("MainWindowv", "64"))
        # 下拉式表單選項 : exchange epochs set
        self.comboBox_3.setItemText(0, _translate("MainWindowv", "0"))
        self.comboBox_3.setItemText(1, _translate("MainWindowv", "5"))
        self.comboBox_3.setItemText(2, _translate("MainWindowv", "10"))
        self.comboBox_3.setItemText(3, _translate("MainWindowv", "50"))
        self.comboBox_3.setItemText(4, _translate("MainWindowv", "100"))
        self.comboBox_3.setItemText(5, _translate("MainWindowv", "300"))
        self.tabWidget_oper.setTabText(self.tabWidget_oper.indexOf(self.tab_6), _translate("MainWindowv", "操作窗口"))

