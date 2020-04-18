from tkinter import *
from datetime import datetime, timedelta
from _thread import start_new_thread
from typing import Tuple, List
import string
import colorsys
import copy
from statistics import mean, StatisticsError
sensor_points = {}

config={
    "screenX":1280,
    "screenY":1000,
    "screenTitle":"Tellus"
}
window = Tk()
window.title(config["screenTitle"])
canvas = Canvas(window, width=config["screenX"],height=config["screenY"],background="white")
canvas.pack()
textField = canvas.create_text(100,10,text="Time")
textField2 = canvas.create_text(40,60,text="Latest reading", anchor=SW)
def mapFromTo(x,a,b,c,d):
    y=(x-a)/(b-a)*(d-c)+c
    return y

def update_sensor_point(id,  xy, value, timestamp):
    global sensor_points
    canvas.itemconfigure(textField, text = str(timestamp))
    
    try:
        canvas.itemconfigure(textField2, text = "Latest reading: "+ str(value)+"*C.\n Current average: "+str(round(mean([x[2] for x in sensor_points.values()]),2)))
    except StatisticsError:
        pass
    min_hsl = (228/360, 1, .50)
    max_hsl = (360/360, 1, .50)
    progress = mapFromTo(value, 18,25,min_hsl[0],max_hsl[0])
    #print(progress)
    color = colorsys.hls_to_rgb(progress,0.5,1)
    #print(color)
    if id not in sensor_points:
        sensor_points[id] = [canvas.create_oval(xy[0]-8,xy[1]-8,xy[0]+8,xy[1]+8, fill='#%02x%02x%02x' % (int(color[0]*255),int(color[1]*255),int(color[2]*255))), timestamp, value, canvas.create_text(xy[0]+20,xy[1]+3,text=value)]
    else:
        canvas.itemconfig(sensor_points[id][0], fill='#%02x%02x%02x' % (int(color[0]*255),int(color[1]*255),int(color[2]*255)) )
        sensor_points[id][1]=timestamp
        sensor_points[id][2]=value
        canvas.itemconfigure(sensor_points[id][3], text = str(value))
    new_dict = sensor_points
    copied=False
    for key,value in sensor_points.items():
        
        if value[1]+timedelta(minutes = 60) < timestamp:
            if not copied:
                copied=True
                new_dict = copy.deepcopy(sensor_points)
            canvas.delete(sensor_points[id][0])
            canvas.delete(sensor_points[id][3])
            del new_dict[key]
    if copied: sensor_points=new_dict
    
    #print(sensor_points)
def updateState(points):
   
    for point in points:
       # print(point)
        textField = canvas.create_text(point[0][0]+16,point[0][1]-8,text=point[1])
       
        canvas.create_oval(point[0][0],point[0][1],point[0][0]+1,point[0][1]+1,fill="black")
