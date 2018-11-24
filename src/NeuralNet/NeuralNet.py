import torch 
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
import pandas as pd
from src import *
import numpy as np
import sys
import json
import math

my_input_de_prueba = [WET,FREEZE,HOT,WET,FREEZE,HOT,NICE, GLOOMY, WET,FREEZE, WET,FREEZE,HOT,NICE, GLOOMY, HOT,WET,FREEZE, WET,FREEZE,HOT,NICE, GLOOMY, HOT,NICE, GLOOMY,NICE, GLOOMY,WET,FREEZE, WET,FREEZE,HOT,NICE, GLOOMY, HOT,WET,FREEZE,HOT,NICE, GLOOMY,NICE, GLOOMY,NICE,WET,FREEZE,HOT,WET,FREEZE,HOT,NICE, GLOOMY,NICE, GLOOMY, GLOOMY,WET,FREEZE,HOT,WET,FREEZE,HOT,NICE, GLOOMY,NICE, GLOOMY]


class LinearRegression(nn.Module):
    def __init__(self,n_in,n_out):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(n_in,n_out)

    def forward(self,x):
        out = self.linear(x) #Forward propagation 
        return out

#ESTE DATASET EN TEORÍA TENDRÍA SENTIDO
def generate_train_data():
    my_x = []
    my_y = []

    for i in range(len(my_input_de_prueba)):
        my_x.append(generate_numpyarray(my_input_de_prueba[i]))
        my_y.append(get_features2(my_input_de_prueba[i]))

    return my_x, my_y    


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

def generate_numpyarray(tiempo):
    if(tiempo == WET):
        a = np.array([1.,0.,0.,0.,0.])
    elif(tiempo == HOT):
       a=  np.array([0.,1.,0.,0.,0.])
    elif(tiempo == FREEZE):
       a=  np.array([0.,0.,1.,0.,0.])
    elif(tiempo == GLOOMY):
        a= np.array([0.,0.,0.,1.,0.])
    else 
        a= np.array([0.,0.,0.,0.,1.])
    


# def train(path_to_store_weight_file, number_of_iterations=1):
def train(number_of_iterations=1):
    #mirar cuando este mas despierto
    n_in, n_out = 5,4

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
        targets = targets.view(1,4)
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
    model.save_state_dict('./model.pt')



def test(test_data):
    model.load_state_dict(torch.load('./model.pt'))
    y_pred = model(test_data)
    return y_pred.data

#los sentimientos pueden ser 5 = SAD,HAPPY,ANGRY,BORED,TIRED
#las posibilidades de weather pueden ser 5 WET GLOOMY (fog) FREEZE HOT NICE 


#tempo -> float bpm
#instrumentalness from 0.5 to 1.0 (non vocal content)
#ENERGY from 0.0 to 1.0 (1.0 is high energy like Death Metal)
#DANCEABILITY from 0.0 to 1.0 (1.0 is really danceable)
def get_features(y):
    res = dict()
    if(y==WET):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        res = json.dumps(res)
        return res
    elif(y==NICE):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        res = json.dumps(res)
        return res
    elif(y==GLOOMY):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        res = json.dumps(res)
        return res
     elif(y==HOT):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        res = json.dumps(res)
        return res
     elif(y==FREEZE):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        res = json.dumps(res)
        return res
    
    
def get_features2(y):
    if(y==WET):
        tempo =sigmoid()
        instrumentalness= 
        danceability=
        energy =    
        a = np.array([tempo,instrumentalness,danceability,energy])
        return a
    elif(y==NICE):
        tempo =sigmoid()
        instrumentalness= 
        danceability=
        energy = 
        a = np.array([tempo,instrumentalness,danceability,energy])   
        return a
    elif(y==GLOOMY):
        tempo =sigmoid()
        instrumentalness= 
        danceability=
        energy = 
        a = np.array([tempo,instrumentalness,danceability,energy])   
        return a
     elif(y==HOT):
        tempo =sigmoid()
        instrumentalness= 
        danceability=
        energy = 
        a = np.array([tempo,instrumentalness,danceability,energy])   
        return a
     elif(y==FREEZE):
        tempo =sigmoid()
        instrumentalness= 
        danceability=
        energy = 
        a = np.array([tempo,instrumentalness,danceability,energy])   
        return a


#SPOTIFY URI WHERE WE PICK THE VALUES 

wet= 'spotify:track:0mPVXHJ4Aibai5VA0F4Lwa'
gloomy= 'spotify:track:3JOVTQ5h8HGFnDdp4VT3MP'
freeze='spotify:track:6JfGyDX7mlvV6Ij3j4tm9q'
hot='spotify:track:1H5tvpoApNDxvxDexoaAUo'
nice='spotify:track:0tZkVZ9DeAa0MNK2gY5NtV'


if __name__ == "__main__":
    train(1000)
    # if sys.argv[1] == "train":
    #     #path donde guardar los pesos y numero de iteraciones 
    #     train(sys.argv[2], int(sys.argv[3]))
