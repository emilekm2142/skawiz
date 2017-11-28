import time
import datetime
import random
from math import sin
SENSORS_COUNT = 6
def get_data():
    ret = []
    for i in range(SENSORS_COUNT):
        now = datetime.datetime.now().time().second*1000 + datetime.datetime.now().time().microsecond
        now  = now/1000 # sekundy
        val = 10
        val += 100.0 * (1 + sin( 2.0 * 3.14159 * (i+1)*0.02 * now ))
        val += random.randint(0,10)
        ret.append(val)
    return ret