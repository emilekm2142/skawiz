import gui
from scipy.interpolate import interp1d
from gui import config
from getData import get_data,vary_point
from time import sleep
import pandas as pd
from dateutil import parser
from datetime import datetime, timedelta
from _thread import start_new_thread
data_file = open("data.csv", 'r')
current_time = parser.parse("2017-06-26 10:26:02.779")



translate_to_screen = lambda distance: int(distance)
center = config["screenX"]/2
leftTopCorner = (65.05860348, 25.46612754)
leftBottomCorner = (65.05860430 ,25.46470780)

rightTopCorner = (65.05892835,25.46612620)
rightBottomCorner = (65.05892835,25.46471000)
corners = [leftTopCorner, leftBottomCorner, rightTopCorner, rightBottomCorner]
def load_sensors_data(filename):
    handle = open(filename, 'r')
    d={}
    for line in handle:
        k = line.split("\t")
        d[k[1]] = (float(k[3].replace(",",'.')), float(k[4].replace(",",'.')), k[2].split("-")[0])
    handle.close()
    return d
sensors = load_sensors_data("sensors.csv")

def mapFromTo(x,a,b,c,d):
    y=(x-a)/(b-a)*(d-c)+c
    return y
mapToScreen = lambda x: (mapFromTo(x[0], min([d[0] for d in corners]),max([d[0] for d in corners]),0,1) * (720+200), mapFromTo(x[1], min([d[1] for d in corners]),max([d[1] for d in corners]),0,1)*(1000) )

def main():
    gui.updateState([(mapToScreen(x),x[2]) for x in sensors.values()])


line_range = [0,400]
def get_temperature_for_sensor(key,current_time):
    pass
def main_loop():
    global current_time
    i=0
    for line in data_file:
        i+=1 
        if i<500000: continue
        if "timestamp,co2,humidity" in line : continue
       
        values = line.split(",")
        time= parser.parse(values[-6])
        tmp = values[-2]
        sensor_id = values[0].replace("-", '').upper()
       
        try:
            gui.update_sensor_point(sensor_id, mapToScreen(sensors[sensor_id]), float(tmp),time)
        except KeyError:
            pass
            #print("no such sensor: ", sensor_id)
    # while True:
    #     current_time+=timedelta(seconds=60)
    #     gui.updateState([mapToScreen(value)+get_temperature_for_sensor(key, current_time) for key,value in sensors.items()])
    #     sleep(0.2)

gui.window.after(0, main)
start_new_thread(main_loop,())
gui.window.mainloop()