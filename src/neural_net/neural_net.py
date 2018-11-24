from src import *
import torch 
import torch.nn as nn
import random
import torch.optim as optim
from torch.autograd import Variable
import matplotlib.pyplot as plt 
import numpy as np
import sys
import json
import math





my_input_de_prueba = [WET,FREEZE,HOT,WET,FREEZE,HOT,NICE, GLOOMY, WET,FREEZE, WET,FREEZE,HOT,NICE, GLOOMY, HOT,WET,FREEZE, WET,FREEZE,HOT,NICE, GLOOMY, HOT,NICE, GLOOMY,NICE, GLOOMY,WET,FREEZE, WET,FREEZE,HOT,NICE, GLOOMY, HOT,WET,FREEZE,HOT,NICE, GLOOMY,NICE, GLOOMY,NICE,WET,FREEZE,HOT,WET,FREEZE,HOT,NICE, GLOOMY,NICE, GLOOMY, GLOOMY,WET,FREEZE,HOT,WET,FREEZE,HOT,NICE, GLOOMY,NICE, GLOOMY]
my_input_de_test = [GLOOMY, NICE, FREEZE,HOT, WET]

#MODEL
class LinearRegression(nn.Module):
    def __init__(self,n_in,n_out):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(n_in,n_out)

    def forward(self,x):
        out = self.linear(x) #Forward propagation 
        return out

#ESTE DATASET EN TEORÍA TENDRÍA SENTIDO
def generate_data():
    my_x = []
    my_y = []

    for i in range(len(my_input_de_prueba)):
        my_x.append(generate_numpyarray(my_input_de_prueba[i]))
        my_y.append(get_features2(my_input_de_prueba[i],random.randint(0, 1)))
    return my_x, my_y    

def generate_data_tests():
    my_x= []
    for i in range(len(my_input_de_test)):
        my_x.append(generate_numpyarray(my_input_de_test[i]))
    return my_x



#SQUASHING FUNCTION
def sigmoid(x):
  return 1 / (1 + math.exp(-x))


#DATASET DE PRUEBA DE ARRAYS RANDOMS DE 0 y 1
def generate_data_set_prova():
    my_x = []
    my_y = []

    for x in range(1):
        a = np.eye(5,dtype=float)
        np.random.shuffle(a)
        my_x.append(a[0])
        
        d = np.eye(4,dtype=float)
        np.random.shuffle(d)
        my_y.append(d[0])
 
    return my_x,my_y


#GENERATE NUMPY ARRAYS DEPENDING THE TIME CONDITIONS
def generate_numpyarray(tiempo):
    if tiempo == WET:
        a = np.array([1.,0.,0.,0.,0.],dtype=float)
    elif tiempo == HOT:
       a=  np.array([0.,1.,0.,0.,0.],dtype=float)
    elif tiempo == FREEZE:
       a=  np.array([0.,0.,1.,0.,0.],dtype=float)
    elif tiempo == GLOOMY:
        a= np.array([0.,0.,0.,1.,0.],dtype=float)
    else :
        a= np.array([0.,0.,0.,0.,1.],dtype=float)
    return a


def train(number_of_iterations=1):
    n_in, n_out = 5,4
    model = LinearRegression(n_in,n_out) 

    #Lost and Optimizer
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(),lr=0.01)

    inputs, outputs = generate_data()

    for t in range(number_of_iterations):
        #convert numpy array to tensor 
        inputs = Variable(torch.as_tensor(inputs).float())
        targets = Variable(torch.as_tensor(outputs).float())
        y_pred = model(inputs)
        targets = targets.view(len(inputs),4)
        loss_fn = criterion(y_pred,targets)

        #letsdosome gradient
        optimizer.zero_grad()
        loss_fn.backward()
        optimizer.step()
        plot[t] = loss_fn.item()
        #devolver el error 
        print('Iteration '+str(t)+': ',loss_fn.item())

    print('DONE')
    torch.save(model.state_dict(),('./model.pt'))
    print('Guardado')



def test():
    model = LinearRegression(5,4) 
    model.load_state_dict(torch.load('./model.pt'))
    inputs = generate_data_tests()
    inputs = Variable(torch.as_tensor(inputs).float())
    y_pred = model(inputs)
    print(y_pred.data)
    return y_pred

def get_features(y):
    res = dict()
    if y==WET:
        res["tempo"] = (123.844)
        res["instrumentalness"]=0.883
        res["energy"]=0.344
        res["danceability"]=0.576
        res = json.dumps(res)
        return res
    elif y==NICE:
        res["tempo"] = (118.05)
        res["instrumentalness"]=0.00000583
        res["energy"]=0.792
        res["danceability"]= 0.829
        res = json.dumps(res)
        return res
    elif y==GLOOMY:
        res["tempo"] = (174.117)
        res["instrumentalness"]=0.000366
        res["energy"]=0.0581
        res["danceability"]=0.345
        res = json.dumps(res)
        return res
    elif y==HOT:
        res["tempo"] = (129.221)
        res["instrumentalness"]=0
        res["energy"]=0.887
        res["danceability"]=0.869
        res = json.dumps(res)
        return res
    elif y==FREEZE:
        res["tempo"] = (128.993)
        res["instrumentalness"]=0.888
        res["energy"]=0.175
        res["danceability"]=0.371
        res = json.dumps(res)
        return res
            
    
def get_features2(y,i):
    if y==WET:
        if(i==0):
            tempo = (123.844) 
            instrumentalness= 0.883
            energy= 0.344
            danceability= 0.576
        else :
            tempo = 84.996
            instrumentalness=0
            danceability = 0.642
            energy = 0.289
        a = np.array([tempo,instrumentalness,danceability,energy])
        return a
    elif y==NICE:
        if(i==0):
            energy = 0.457
            tempo=150.953
            danceability=0.686
            instrumentalness=0
        else:
            tempo = (118.05)
            instrumentalness=0.00000583
            energy=0.792
            danceability= 0.829
        a = np.array([tempo,instrumentalness,danceability,energy])   
        return a
    elif y==GLOOMY:
        tempo = (174.117)
        instrumentalness=0.000366
        energy=0.0581
        danceability=0.345
        a = np.array([tempo,instrumentalness,danceability,energy])   
        return a
    elif y==HOT:
        tempo = (129.221)
        instrumentalness=0
        energy=0.887
        danceability=0.869
        a = np.array([tempo,instrumentalness,danceability,energy])   
        return a
    elif y==FREEZE:
        tempo = (128.993)
        instrumentalness=0.888
        energy=0.175
        danceability=0.371
        a = np.array([tempo,instrumentalness,danceability,energy])   
        return a


def plots(a):
    # plt.bar(range(len(plot)), list(plot.values()), align='center')
    # plt.xticks(range(len(plot)), list(plot.keys()))
    # plt.show()

    plot = dict()
    
    #GLOOMY PLOT
    performance = [a[0][1],a[0][2],a[0][3]]
    objects =('Instrumentalness','Energy','Danceability')
    plt.bar(np.arange(len(objects)), performance, align='center', alpha=0.5)
    plt.xticks(np.arange(len(objects)), objects)
    plt.ylabel('Value')
    plt.title('Gloomy')
    plt.show()

    #NICE PLOT
    performance = [c, a[1][1],a[1][2],a[1][3]]
    objects =('Instrumentalness','Energy','Danceability')
    plt.bar(np.arange(len(objects)), performance, align='center', alpha=0.5)
    plt.xticks(np.arange(len(objects)), objects)
    plt.ylabel('Value')
    plt.title('Nice')
    plt.show()

    #FREEZE PLOT
    performance = [a[2][1],a[2][2],a[2][3]]
    objects =('Instrumentalness','Energy','Danceability')
    plt.bar(np.arange(len(objects)), performance, align='center', alpha=0.5)
    plt.xticks(np.arange(len(objects)), objects)
    plt.ylabel('Value')
    plt.title('Freeze')
    plt.show()

    #HOT PLOT
    performance = [a[3][1],a[3][2],a[3][3]]
    objects =('Instrumentalness','Energy','Danceability')
    plt.bar(np.arange(len(objects)), performance, align='center', alpha=0.5)
    plt.xticks(np.arange(len(objects)), objects)
    plt.ylabel('Value')
    plt.title('Hot')
    plt.show()

     #WET PLOT
    performance = [a[4][1],a[4][2],a[4][3]]
    objects =('Instrumentalness','Energy','Danceability')
    plt.bar(np.arange(len(objects)), performance, align='center', alpha=0.5)
    plt.xticks(np.arange(len(objects)), objects)
    plt.ylabel('Value')
    plt.title('Hot')
    plt.show()





#SPOTIFY URI WHERE WE PICK THE VALUES 

wet= 'spotify:track:0mPVXHJ4Aibai5VA0F4Lwa'
gloomy= 'spotify:track:3JOVTQ5h8HGFnDdp4VT3MP'
freeze='spotify:track:6JfGyDX7mlvV6Ij3j4tm9q'
hot='spotify:track:1H5tvpoApNDxvxDexoaAUo'
nice='spotify:track:0tZkVZ9DeAa0MNK2gY5NtV'



if __name__ == "__main__":
    train(3000)
    a = test()
    plots(a.detach().numpy())



    # if sys.argv[1] == "train":
    #     #path donde guardar los pesos y numero de iteraciones 
    #     train(sys.argv[2])
    # if sys.argv[1] == "test":
    #     test(test_data)

#tensor([[0.4749, 0.1475, 0.4253, 0.4014],
        # [1.0499, 0.0119, 0.5513, 0.5331],
        # [0.9689, 0.3906, 0.2744, 0.2109],
        # [0.8143, 0.3371, 0.9320, 0.2388]])
