import torch 
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
import pandas as pd
import numpy as np
import sys


class LinearRegression(nn.Module):
    def __init__(self,n_in,n_out):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(n_in,n_out)

    def forward(self,x):
        out = self.linear(x) #Forward propagation 
        return out

#DATASET
# aqui me tengo creado dos vectores de prueba que me sirven de dataset, en el my_x hay un vector de 5 dimensiones 
# que me representan las 5 posibilidades de weather y en my_y hay un vector de 4 dimensiones con las 4 posibilidades
# de sentimientos

def generate_data_set_prova():
    my_x = []
    my_y = []

    for x in range(10000):
        a = np.eye(5,dtype=float)
        np.random.shuffle(a)
       
       #se que debería ser 4 pero el puto modelo me pide las mismas
        b = np.eye(5,dtype=float)
        np.random.shuffle(b)
        
        c = [a[0],b[0]]
        my_x.append(c)
        
        d = np.eye(4,dtype=float)
        np.random.shuffle(d)
        my_y.append(d[0])
 
    return my_x,my_y


# def train(path_to_store_weight_file, number_of_iterations=1):
def train(number_of_iterations=1):
    #mirar cuando este mas despierto
    n_in, n_out = 5,2

    #tengo 14 outputs son 7 features y rango
    model = LinearRegression(n_in,n_out) 
    #Lost and Optimizer
    #me dicen que tengo que usar la cross entropy
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(),lr=0.01)


    #vamos a pillar lo que he generado en el generate
    inputs, outputs = generate_data_set_prova()

    for t in range(number_of_iterations):
        #convert numpy array to tensor 
        inputs = Variable(torch.as_tensor(inputs).float())
        targets = Variable(torch.as_tensor(outputs).float())
        y_pred = model(inputs)
        targets = targets.view(10000,2,2)
        loss_fn = criterion(y_pred,targets)
        #letsdosome gradient
        optimizer.zero_grad()
        loss_fn.backward()
        optimizer.step()
        #devolver el error 
        print('Iteration '+str(t)+': ',loss_fn.item())
        # if((t+1) %5 == 0) :
        #     predicted = model(Variable(torch.as_tensor(inputs).float()).data.numpy()
        #     plt.plot(x_train,y_train,label='Original Data')
        #     plt.plot(x_train,predicted,label='Fitted Line')
        #     plt.legend()
        #     plt.show()

    print('DONE')
    # torch.save(model,path_to_store_weight_file)



def test(path_to_load_weight_file=None, path_to_test_data=None):
    # file_to_open = path_to_test_data + "test_data.txt"
    # f = open(file_to_open).read()
    y_pred = model(x.float())
    #transforming a torch tensor to a numpyarray
    y_pred = y_pred.data.numpy()
    print(y_pred)
    #creating a panda dataframe from the numpy array
    pd.DatFrame(y_pred)
    print(pd)


if __name__ == "__main__":
    train(10000)
    # if sys.argv[1] == "train":
    #     #path donde guardar los pesos y numero de iteraciones 
    #     train(sys.argv[2], int(sys.argv[3]))
