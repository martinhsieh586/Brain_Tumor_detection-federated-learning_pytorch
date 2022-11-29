import numpy as np
import torch
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import random
import os

# 借用tensorflow的影像處理函式庫
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.utils import to_categorical

# 用來儲存樣本的函式庫
import pickle # serialization
# train test split
from sklearn.model_selection import train_test_split

def Image_to_Array(pic, width, height):
    image = load_img(pic, target_size=(width, height),color_mode='grayscale')
    image_array = img_to_array(image)
    image_preprocess = preprocess_input(image_array) # normalize the value of each element in array
    return  image_preprocess
pass

def load_pictures(picdir, width_size, height_size):
    # init variables to store sample
    x_data = []
    y_labels = []

    for dirPath, _, fileNames in os.walk(picdir):
        # get y (ans)
        pil_name = dirPath.split('/')
        if pil_name[-1] != '':
            ans = pil_name[-1]
            del pil_name
        else:
            continue
        for f in fileNames:
            # get x (picture)
            PicDir = os.path.join(dirPath, f)
            NArray_2D  = Image_to_Array(PicDir,width_size,height_size)

            # store y, x
            y_labels.append(ans)
            x_data.append(NArray_2D)
    return y_labels, x_data

def encode_data(i_y, i_x, i_dim):
    # convert the data and labels to NumPy arrays
    x_data = np.array(i_x, dtype="float32")
    y_labels = np.array(i_y)
    #################################################
    # perform one-hot encoding on the labels
    # from 3 to [0,0,0,1,0,0,0,0,0,0]
    #################################################
    y_labels3 = to_categorical(y_labels,i_dim)

    return y_labels3, x_data
pass

# 把眾多照片存成一個檔案
def save_sample(i_y, i_x, i_filename):
    f = open(i_filename, 'wb')
    pickle.dump([i_y,i_x], f)
    f.close()
pass

# 把那一個檔案中讀出來眾多照片
def load_sample(i_filename):
    f = open(i_filename, 'rb')
    r = pickle.load(f)
    y_labels = r[0]
    x_data = r[1]
    return y_labels, x_data
pass

# 在眾多照片中隨機抽樣
def get_sample(i_y, i_x, i_sample_size):
    ##############################
    # get training data randomly

    # init x batch and y batch
    x_batch=[]
    y_batch=[]

    sample = random.sample(range(len(i_y)), i_sample_size)

    x_batch = [i_x[i] for i in sample]
    y_batch = [i_y[i] for i in sample]

    return np.array(y_batch), np.array(x_batch)
pass

# 抽樣完後，把照片轉成tensor格式
def Image_to_Tensor(pic, width_size, height_size, depth_size=1):
    image = None
    if depth_size == 1: # 黑白
        image = load_img(pic, target_size=(width_size, height_size),color_mode='grayscale')
    else : # 彩色
        image = load_img(pic, target_size=(width_size,height_size))
    pass
    image_array = img_to_array(image)
    image_preprocess = preprocess_input(image_array) # normalize the value of each element in array
    # x.reshape(batch, width, height, bw=1) color=4
    x = image_preprocess.reshape(-1, width_size,height_size,depth_size)
    x = np.transpose(x, (0, 3, 1, 2))
    x = torch.from_numpy(x).float()
    return x
pass

# img_dir:data dir,**file.p**, width_size:int, height_size:int, output:class,int
def envset(img_dir,ori_dir,pil_name,width_size=80,height_size=80,output_dim=4):
    if img_dir is None:
        y_labels, x_data = load_pictures(ori_dir, width_size, height_size)
        save_sample(y_labels, x_data, ori_dir+pil_name+'.p')
    label, img = load_sample(ori_dir+pil_name+'.p')
    y_labels, x_img = encode_data(label, img, output_dim)
    return y_labels, x_img
