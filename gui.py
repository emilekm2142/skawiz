from tkinter import *
from _thread import start_new_thread
points = []
config={
    "screenX":300,
    "screenY":500,
    "screenTitle":"SKA"
}
window = Tk()
window.title(config["screenTitle"])
canvas = Canvas(window, width=config["screenX"],height=config["screenY"],background="white")
canvas.pack()
def draw_point(new_point:tuple):
    points.append(canvas.create_rectangle(new_point[0],new_point[1],new_point[0]+1,new_point[1]+1,fill="black"))
def get_coordinates(p):
    try:
        return (int(canvas.coords(p)[0]),int(canvas.coords(p)[1]))
    except IndexError:
        return None
def find_point(point):
    try:
        for p in points:
            if int(canvas.coords(p)[0]) == c[0] and int(canvas.coords(p)[1]) == c[1]:
                return p
    except:
        pass
def delete_point(c:tuple):
    try:
        for p in points:
            if int(canvas.coords(p)[0]) == c[0] and int(canvas.coords(p)[1]) == c[1]:
                canvas.delete(p)
                points.remove(p)
                break
       # point = [p for p in points if int(canvas.coords(p)[0]) == c[0] and int(canvas.coords(p)[1]) == c[1]]
        #print(point)
        #canvas.delete(point[0])
    except IndexError:
        pass