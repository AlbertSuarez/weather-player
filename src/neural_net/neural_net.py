
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

from src import *



#TESTING INPUT OF TRAINING AND TESTING
my_input_de_prueba = [WET, GLOOMY, HOT,WET,FREEZE, WET,FREEZE,HOT,NICE, GLOOMY, HOT,NICE, GLOOMY,NICE, GLOOMY,WET,FREEZE, WET,FREEZE,HOT,NICE, GLOOMY, HOT,WET,FREEZE,HOT,NICE, GLOOMY,NICE, GLOOMY,NICE,WET,FREEZE,HOT,WET,FREEZE,HOT,NICE, GLOOMY,NICE, GLOOMY, GLOOMY,WET,FREEZE,HOT,WET,FREEZE,HOT,NICE, GLOOMY,NICE, GLOOMY]
my_input_de_test = [GLOOMY, NICE, FREEZE,HOT,WET]

#MODEL
class LinearRegression(nn.Module):
    def __init__(self,n_in,n_out):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(n_in,n_out)

    def forward(self,x):
        out = self.linear(x) 
        return out

#GENERATE THE DATA INPUT AND OUTPUT FOR THE TRAINING
def generate_data():
    my_x = []
    my_y = []

    for i in range(len(my_input_de_prueba)):
        my_x.append(generate_numpyarray(my_input_de_prueba[i]))
        my_y.append(get_features2(my_input_de_prueba[i]))
    return my_x, my_y    

#GENERATING THE DATA INPUT FOR THE EXECUTION
def generate_data_execute(valores):
    my_x= []
    for i in range(len(valores)):
        my_x.append(generate_numpyarray(valores[i]))
    return my_x


#SQUASHING FUNCTION
def sigmoid(x):
  return 1 / (1 + math.exp(-x))


#RANDOM NONSENSE DATASET FOR TESTING STUFF
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

#training
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

        #lets do some gradient
        optimizer.zero_grad()
        loss_fn.backward()
        optimizer.step()
        print('Iteration '+str(t)+': ',loss_fn.item())

    print('DONE')
    torch.save(model.state_dict(),('./model2.pt'))
    print('Guardado')



#testing part
def test():
    model = LinearRegression(5,4) #check this stuff
    model.load_state_dict(torch.load('./model2.pt'))
    inputs = generate_data_execute(my_input_de_test)
    inputs = Variable(torch.as_tensor(inputs).float())
    y_pred = model(inputs)
    return y_pred


#execute function that it is going to be called from player.py
def execute(valores):
    diccionari =dict()
    model = LinearRegression(5,4) #check this stuff
    model.load_state_dict(torch.load('./model2.pt'))
    inputs = generate_data_execute(valores)
    inputs = Variable(torch.as_tensor(inputs).float())
    y_pred = model(inputs)
    y = y_pred.detach().numpy().tolist()
    diccionari["tempo"]= y[0][0]
    diccionari["instrumentalness"]= y[0][1]
    diccionari["danceability"]=y[0][2]
    diccionari["energy"]=y[0][3]
    print(diccionari)
    return diccionari


#get features in a json object, NOT USED NOW
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
            
    
#get features in a numpy array 
def get_features2(y):
    if y==WET:
        i = random.randint(0, 7)
        if(i==0):
            tempo = (123.844) 
            instrumentalness= 0.883
            energy= 0.344
            danceability= 0.576
        elif(i==1) :
            tempo = 84.996
            instrumentalness=0
            danceability = 0.642
            energy = 0.289
        elif(i==2):
            tempo=138.265
            instrumentalness=0.00195
            energy=0.418
            danceability= 0.209
        elif(i==3):
            tempo = 132.0
            instrumentalness=0.898
            danceability=0.544
            energy=0.0508
        elif(i==4):
            tempo= 83.14
            danceability= 0.521
            energy=0.336
            instrumentalness=0.0121
        elif(i==5):
            tempo = 159.646
            danceability=0.35
            energy=0.42
            instrumentalness=0.898
        elif(i==6):
            tempo=159.646
            energy=0.42
            danceability=0.35
            instrumentalness=0.898
        else:
            danceability=0.64
            energy=0.743
            instrumentalness=0
            tempo=122.035
        
        a = np.array([tempo,instrumentalness,danceability,energy])

        return a

    elif y==NICE:
        i = random.randint(0, 5)
        if(i==0):
            energy = 0.457
            tempo=150.953
            danceability=0.686
            instrumentalness=0
        elif(i==1):
            tempo = (118.05)
            instrumentalness=0.00000583
            energy=0.792
            danceability= 0.829
        elif(i==2):
            tempo = 138.265
            danceability=0.209
            energy=0.418
            instrumentalness= 0.00195
        elif(i==3):
            tempo=120.175
            energy=0.376
            danceability=0.584
            instrumentalness=0
        elif(i==4):
            tempo=147.21
            energy=0.607
            danceability=0.386
            instrumentalness=0
        else:
            tempo=116.047
            danceability=0.794
            instrumentalness=0
            energy=0.811
        a = np.array([tempo,instrumentalness,danceability,energy])   
        return a

    elif y==GLOOMY:
        i = random.randint(0, 4)
        if(i==0):
            tempo =174.117
            instrumentalness=0.000366
            energy=0.0581
            danceability=0.345
        elif(i==1):
            tempo=77.748
            instrumentalness=0
            danceability=0.581
            energy=0.163
        elif(i==2):
            tempo=166.467
            instrumentalness=0
            energy=0.29
            danceability=0.379
        elif(i==3):
            tempo=109.942
            instrumentalness=0.619
            energy=0.585
            danceability=0.775
        else:
            danceability=0.38
            energy=0.846
            tempo=89.98
            instrumentalness=0.611
        a = np.array([tempo,instrumentalness,danceability,energy])   
        return a
    elif y==HOT:
        i = random.randint(0, 3)
        if(i==0):
            tempo = (129.221)
            instrumentalness=0
            energy=0.887
            danceability=0.869
        elif(i==1):
            tempo=159.911
            instrumentalness=0
            energy=0.757
            danceability=0.652
        elif(i==2):
            tempo=106.978
            instrumentalness= 0
            danceability=0.576
            energy=0.579
        else:
            tempo=105.13
            instrumentalness=0
            danceability=0.757
            energy=0.899

        a = np.array([tempo,instrumentalness,danceability,energy])   
        return a

    elif y==FREEZE:
        i = random.randint(0, 3)
        if(i==0):
            tempo = 128.993
            instrumentalness=0.888
            energy=0.175
            danceability=0.371
        elif(i==1):
            tempo=130.29
            energy=0.36
            instrumentalness=0
            danceability=0.599
        elif(i==2):
            tempo=159.871
            energy=0.712
            instrumentalness=0.0
            danceability=0.537
        else:
            tempo=143.808
            energy=0.489
            danceability=0.439
            instrumentalness=0.0
        a = np.array([tempo,instrumentalness,danceability,energy])   
        return a

#this functions gives us plots about each genre and features we are analysing
def plots(a):
    a = a.detach().numpy().tolist()

    #GLOOMY PLOT
    performance = [a[0][1],a[0][2],a[0][3]]
    objects =('Instrumentalness','Energy','Danceability')
    plt.bar(np.arange(len(objects)), performance, align='center', alpha=0.5)
    plt.xticks(np.arange(len(objects)), objects)
    plt.ylabel('Value')
    plt.title('Gloomy')
    plt.show()

    #NICE PLOT
    performance = [a[1][1],a[1][2],a[1][3]]
    objects =('Instrumentalness','Energy','Danceability')
    plt.bar(np.arange(len(objects)), performance, align='center', alpha=0.5)
    plt.xticks(np.arange(len(objects)), objects)
    plt.ylabel('Value')
    plt.title('Nice')
    plt.show()

    # #FREEZE PLOT
    performance = [a[2][1],a[2][2],a[2][3]]
    objects =('Instrumentalness','Energy','Danceability')
    plt.bar(np.arange(len(objects)), performance, align='center', alpha=0.5)
    plt.xticks(np.arange(len(objects)), objects)
    plt.ylabel('Value')
    plt.title('Freeze')
    plt.show()

    # #HOT PLOT
    performance = [a[3][1],a[3][2],a[3][3]]
    objects =('Instrumentalness','Energy','Danceability')
    plt.bar(np.arange(len(objects)), performance, align='center', alpha=0.5)
    plt.xticks(np.arange(len(objects)), objects)
    plt.ylabel('Value')
    plt.title('Hot')
    plt.show()

    #  #WET PLOT
    performance = [a[4][1],a[4][2],a[4][3]]
    objects =('Instrumentalness','Energy','Danceability')
    plt.bar(np.arange(len(objects)), performance, align='center', alpha=0.5)
    plt.xticks(np.arange(len(objects)), objects)
    plt.ylabel('Value')
    plt.title('Wet')
    plt.show()

#SPOTIFY URI WHERE WE PICK THE VALUES 

wet= 'spotify:track:0mPVXHJ4Aibai5VA0F4Lwa'
gloomy= 'spotify:track:3JOVTQ5h8HGFnDdp4VT3MP'
freeze='spotify:track:6JfGyDX7mlvV6Ij3j4tm9q'
hot='spotify:track:1H5tvpoApNDxvxDexoaAUo'
nice='spotify:track:0tZkVZ9DeAa0MNK2gY5NtV'



# if __name__ == "__main__":
#     train(6500)
#     res = test()
#     plots(res)


#     print("WET weather")
#     execute(["wet"])
    
#     print("NICE weather")
#     execute(["nice"])

#     print("GLOOMY weather")
#     execute(["gloomy"])
    
#     print("FREEZE weather")
#     execute(["freeze"])
    
#     print("HOT  weather")
#     execute(["hot"])
    
    
    
   

 