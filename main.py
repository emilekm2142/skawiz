import gui

def main():
    gui.draw_point((15,15))
    for i in range(50):
        print(i)
        gui.draw_point((i, i))

    for i in range(50):

        gui.delete_point((i,i))



gui.window.after(0, main)
gui.window.mainloop()
