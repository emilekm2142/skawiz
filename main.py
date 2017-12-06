import gui
from gui import config
from getData import get_data,vary_point
from time import sleep
from _thread import start_new_thread
translate_to_screen = lambda distance: int(distance)
center = config["screenX"]/2
def main():
    points = get_data()
    for point in points:
        gui.draw_point((center,translate_to_screen(point)))

def vary():
    while True:
        print("step")
        new_points=[]
        for point in gui.points:
            p = gui.get_coordinates(point)
            new_points.append(vary_point(p))
            gui.delete_point(p)
            #print("new point: ",new)
        for point in new_points:
            gui.draw_point(point)
        #gui.points=new_points
            
        sleep(2)

gui.window.after(0, main)
start_new_thread(vary,())
gui.window.mainloop()