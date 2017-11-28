import gui
from gui import config
from getData import get_data
translate_to_screen = lambda distance: int(distance)
center = config["screenX"]/2
def main():
    points = get_data()
    for point in points:
        gui.draw_point((center,translate_to_screen(point)))



gui.window.after(0, main)
gui.window.mainloop()