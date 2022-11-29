import numpy as np

def train(model, loss_func, train_loader, epochs, image_size):
    # training
    for i in range(epochs):
        model.train()
        y_train, x_train = train_loader
        # 轉換矩陣 from (batch, width, height, depth)
        #      to  (batch, depth, width, height)
        x_train = x_train.reshape(-1, image_size[0], image_size[1], image_size[2])
        x_train = np.transpose(x_train, (0, 3, 1, 2))
        X_s = model.to_placeholder(x_train)
        Y_s = model.to_placeholder(y_train)
        # get y_pred
        y_prediction=model.forward(X_s)
        # get loss = y - y_pred
        loss = loss_func(Y_s, y_prediction)
        # adjust a,b
        model.backward(loss)
    return model