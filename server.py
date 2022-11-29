import numpy as np
import torch
from sklearn.metrics import accuracy_score
import os
from img_precess import *
import model
import copy

class server_eval:
    def __init__(self):
        self.img_dir= 'data/Brain_Tumor_classify.p'
        self.ori_dir= 'data/Brain_Tumor_classify/'
        self.label, self.image = self.envset()
        self.server_model = model.model_init()
    def test(self, model):
        test_image = model.to_placeholder(self.image)
        test_label = model.to_placeholder(self.label)
        # 評估模型準確率
        model.eval()
        y_test_prediction = model.forward(test_image)
        y_truth = torch.argmax(test_label,dim=1).cpu().detach().numpy()
        y_pred = torch.argmax(y_test_prediction,dim=1).cpu().detach().numpy()
        accuracy = accuracy_score(y_truth,y_pred)
        return accuracy

    def exchange(self, models):
        # Convolutional layer parameter sharing
        for index in self.server_model.op_sampling.keys():
            try:
                # init sum of parameters
                Sum = 0
                # FedAvg
                for model_id in models:
                    Sum += models[model_id].op_sampling[index].weight.data
                Avg = Sum / len(models)
                # model copy parameters
                for model_id in models:
                    models[model_id].op_sampling[index].weight.data.copy_(Avg)
            except:
                continue
        # Linear layer parameter sharing
        for index in self.server_model.op_linear.keys():
            try:
                # init sum of parameters
                Sum = 0
                # FedAvg
                for model_id in models:
                    Sum += models[model_id].op_linear[index].weight.data
                Avg = Sum / len(models)
                # model copy parameters
                for model_id in models:
                    models[model_id].op_linear[index].weight.data.copy_(Avg)
            except:
                continue
        best_model = self.models_eval(models)
        # after eval preserve best accuracy
        self.server_model = copy.deepcopy(best_model)

    def models_eval(self, models):
        acc = list()
        for model_id in models:
            acc.append(self.test(models[model_id]))
        best_model = models[list(models)[acc.index(max(acc))]]
        return best_model
    # 測試集載入
    def envset(self, width_size=80, height_size=80, depth_size=1, output_dim=4):
        if not os.path.exists(self.img_dir):
            y_labels_1, x_data_1 = load_pictures(self.ori_dir, width_size, height_size)
            save_sample(y_labels_1, x_data_1, self.img_dir)
        label, img = load_sample(self.img_dir)
        y_labels, x_img = encode_data(label, img, output_dim)
        _sample_y, _sample_x = get_sample(y_labels, x_img, 64)
        # testing data transform
        x_test = _sample_x.reshape(-1, width_size, height_size, depth_size)
        x_test = np.transpose(x_test, (0, 3, 1, 2))
        return _sample_y, x_test
