
from src import *

#los sentimientos pueden ser 5 = SAD,HAPPY,ANGRY,BORED,TIRED
#las posibilidades de weather pueden ser 5 WET GLOOMY (fog) FREEZE HOT NICE 

def get_features(x,y):
    res = dict()
    #CASOS HAPPY
    if(x==HAPPY and y==WET:
        #tempo -> float bpm
        res["tempo"] = 
        #instrumentalness from 0.5 to 1.0 (non vocal content)
        res["instrumentalness"]=
        #from 0.0 to 1.0 (1.0 is high energy like Death Metal)
        res["energy"]=(,)
        #from 0.0 to 1.0 (1.0 is really danceable)
        res["danceability"]=
        return res
    elif(x==HAPPY and y==NICE):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res
    elif(x==HAPPY and y==GLOOMY):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res
     elif(x==HAPPY and y==HOT):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res
     elif(x==HAPPY and y==FREEZE):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res
    
    #CASO SAD
      if(x==SAD and y==WET:
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=(,)
        res["danceability"]=
        return res
    elif(x==SAD and y==NICE):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res
    elif(x==SAD and y==GLOOMY):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res
     elif(x==SAD and y==HOT):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res
     elif(x==SAD and y==FREEZE):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res

    #CASO BORED
      if(x==BORED and y==WET:
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=(,)
        res["danceability"]=
        return res
    elif(x==BORED and y==NICE):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res
    elif(x==BORED and y==GLOOMY):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res
     elif(x==BORED and y==HOT):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res
     elif(x==BORED and y==FREEZE):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res

    #CASO TIRED
      if(x==TIRED and y==WET:
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=(,)
        res["danceability"]=
        return res
    elif(x==TIRED and y==NICE):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res
    elif(x==TIRED and y==GLOOMY):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res
     elif(x==TIRED and y==HOT):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res
     elif(x==TIRED and y==FREEZE):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res

    #CASO ANGRY
    if(x==ANGRY and y==WET:
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=(,)
        res["danceability"]=
        return res
    elif(x==ANGRY and y==NICE):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res
    elif(x==ANGRY and y==GLOOMY):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res
     elif(x==ANGRY and y==HOT):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res
     elif(x==ANGRY and y==FREEZE):
        res["tempo"] = 
        res["instrumentalness"]=
        res["energy"]=
        res["danceability"]=
        return res