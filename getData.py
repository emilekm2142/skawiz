import time
import datetime
import random
from math import sin
SENSORS_COUNT = 6
def get_data()->list:
    ret = []
    for i in range(SENSORS_COUNT):
        now = datetime.datetime.now().time().second*1000 + datetime.datetime.now().time().microsecond
        now  = now/1000 # sekundy
        val = 10
        val += 100.0 * (1 + sin( 2.0 * 3.14159 * (i+1)*0.02 * now ))
        val += random.randint(0,10)
        ret.append(val)
    return ret
def vary_point(point:tuple)->tuple:
    c = [True,False]
    Xmultiplier = 1
    Ymultiplier = 1
    if (random.choice(c)):
        Xmultiplier=-1
    if (random.choice(c)):
        Ymultiplier=-1
    x=point[0];y=point[1]
    return (x+random.randint(0,10)*Xmultiplier, y+random.randint(0,10)*Ymultiplier)