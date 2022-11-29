# pytorch 函式庫
import torch
import torch.nn as nn
import torch.nn.functional as F
from collections import OrderedDict
import torch.optim as optim
import numpy as np

class Graph_pytorch(nn.Module):
    def __init__(self):
        super(Graph_pytorch, self).__init__() # customize model
        self.var = OrderedDict()

        #self.op = OrderedDict()

        self.op_sampling = OrderedDict()
        self.op_linear = OrderedDict()

        self.lr = 0.001 # learning rate
    pass
pass

def Graph_pytorch_set_input_size(self, i_input_size):
    self.NETWORK_INPUT_FRAME_WIDTH = i_input_size[0]
    self.NETWORK_INPUT_FRAME_HEIGHT = i_input_size[1]
    self.NETWORK_INPUT_FRAME_DEPTH = i_input_size[2]
pass
Graph_pytorch.set_input_size=Graph_pytorch_set_input_size

def Graph_pytorch_set_output_size(self, i_output_dim):
    self.NETWORK_OUTPUT_DIM=i_output_dim
pass
Graph_pytorch.set_output_size=Graph_pytorch_set_output_size


def Graph_pytorch_init_op_sampling(self):

    self.op_sampling['dropout'] = nn.Dropout2d(p=0.2)
    # conv 1
    _layer_1_input = self.NETWORK_INPUT_FRAME_DEPTH
    _layer_1_output = 32
    self.op_sampling['conv_1'] =  nn.Conv2d(in_channels=_layer_1_input,
                      out_channels=_layer_1_output,
                      kernel_size=5,
                      stride=2,
                      padding=0,
                      bias=True)

    # pool 1
    filter_w=2
    filter_h=2
    stride_x=2
    stride_y=2
    self.op_sampling['pool_1']  = nn.MaxPool2d((filter_w, filter_h),
                       stride=(stride_x, stride_y),
                       padding=0)

    # conv 2
    _layer_3_input = _layer_1_output
    _layer_3_output = 64
    self.op_sampling['conv_2'] =  nn.Conv2d(in_channels=_layer_3_input,
                      out_channels=_layer_3_output,
                      kernel_size=5,
                      stride=2,
                      padding=0)

    # pool 2
    self.op_sampling['pool_2'] = nn.MaxPool2d((filter_w, filter_h),
                      stride=(stride_x, stride_y),
                      padding=0)
pass
Graph_pytorch.init_op_sampling = Graph_pytorch_init_op_sampling


def Graph_pytorch_get_linear_relation_layer_input_size(self):

    i_x = np.zeros((1,  self.NETWORK_INPUT_FRAME_DEPTH,
            self.NETWORK_INPUT_FRAME_WIDTH,
            self.NETWORK_INPUT_FRAME_HEIGHT),dtype=float)
    x = self.to_placeholder(i_x)
    # 產出經過samping的樣本
    for index, layer in self.op_sampling.items():
        x = layer(x)
    pass

    # 找出經過sampling的樣本的大小

    _batch, _width, _height, _depth = list(x.size())

    # 這個經過sampling的樣本，需要拉平成一維矩陣，才能丟進去線性關係式
    # 線性關係式: linear relation / full connected layer / fc layer
    # 下面的步驟是找出一維矩陣的大小
    self.Linear_Relation_INPUT_SIZE = _width * _height * _depth
pass
Graph_pytorch.get_linear_relation_layer_input_size = Graph_pytorch_get_linear_relation_layer_input_size

def Graph_pytorch_init_op_linear(self):
    # 建立多項式 (fc2) Y=AX+b，其中有300個x，Y是1x10的矩陣
    _input_shape = self.Linear_Relation_INPUT_SIZE # 須根據sampling後的大小來手動設定
    _ouput_shape = self.NETWORK_OUTPUT_DIM
    _hidden_layer_shape_1 = 128

    self.op_linear['fc1'] = nn.Linear(_input_shape, _hidden_layer_shape_1)

    self.op_linear['fc2'] = nn.Linear(_hidden_layer_shape_1, _ouput_shape)
    self.op_linear['softmax'] = nn.Softmax(dim=1)
pass
Graph_pytorch.init_op_linear = Graph_pytorch_init_op_linear


def Graph_pytorch_init_optimizer(self):
    # 指定我們的優化器為 Adam，需要告訴優化器
    # variable是誰(也就是告訴優化器A和b是哪個變數)
    _parameters = []

    for key, value in self.op_sampling.items():
        _parameters.append({'params':value.parameters()})
    pass

    for key, value in self.op_linear.items():
        _parameters.append({'params':value.parameters()})
    pass


    self.optimizer = optim.Adam(_parameters,
                  lr=self.lr, weight_decay=0)
    '''
    self.optimizer = optim.SGD(_parameters, lr=self.lr, momentum=0.00001)

    '''
    '''
    self.optimizer = optim.RMSprop(_parameters,
                    lr=0.001,
                    alpha=0.99,
                    eps=1e-08,
                    weight_decay=0,
                    momentum=0,
                    centered=False)
    '''
pass
Graph_pytorch.init_optimizer = Graph_pytorch_init_optimizer


def Graph_pytorch_forward(self, i_x):

    # (batch, bw color, width, height)
    x = torch.reshape(i_x,(-1,self.NETWORK_INPUT_FRAME_DEPTH
            ,self.NETWORK_INPUT_FRAME_WIDTH
            ,self.NETWORK_INPUT_FRAME_HEIGHT))

    for index, value in self.op_sampling.items():
        x = value(x)
    pass

    _linear_input_shape = self.Linear_Relation_INPUT_SIZE # 須根據sampling後的大小來手動設定
    x = x.view(-1, _linear_input_shape)

    for index, value in self.op_linear.items():
        x = value(x)
    pass
    return x
pass
Graph_pytorch.forward = Graph_pytorch_forward

def Graph_pytorch_to_placeholder(self, i_x):
    return torch.tensor(i_x, requires_grad=False,dtype=torch.float)
pass
Graph_pytorch.to_placeholder = Graph_pytorch_to_placeholder


def Graph_pytorch_backward(self, i_loss):
    # 反向傳播
    i_loss.backward()
    # 更新模型參數
    self.optimizer.step()
    # 清空梯度
    self.optimizer.zero_grad()
pass
Graph_pytorch.backward = Graph_pytorch_backward


def Graph_pytorch_cal_loss(self, Y_sample, Y_prediction):
    error = Y_sample - Y_prediction
    loss = (error ** 2).mean()
    return loss
pass
Graph_pytorch.cal_loss = Graph_pytorch_cal_loss

def model_init(width_size=80, height_size=80, depth_size=1, output_dim=4):
    model = Graph_pytorch()
    model.set_output_size(output_dim)
    model.set_input_size([width_size, height_size, depth_size])
    model.init_op_sampling()
    model.get_linear_relation_layer_input_size()
    model.init_op_linear()
    model.init_optimizer()
    return model
