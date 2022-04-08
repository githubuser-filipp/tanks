from tkinter import *
tk = Tk()
canvas=Canvas(tk,width = 800,height=650)
canvas.pack()
tank=PhotoImage(file="C:\\F-PYTHON\\tanks\\tank.gif")
l_tank =tank.subsample(4,4)
global x
global y
x = 300
y  = 400

#if event.keysym == "Up":
         #canvas.move(1.0.3)
    # canvas.bind_all("<KeyPress-Up>,l_tank")
while True:
    tk.update()
    canvas.create_image(x,y,image=l_tank)




