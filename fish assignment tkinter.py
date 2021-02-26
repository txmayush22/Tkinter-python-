from tkinter import *
root=Tk()


root.geometry("1450x700+0+0")
canvas=Canvas(root,background="white",width=1200,height=700)
#fish
canvasFish=Canvas(root,background="white",width=1200,height=700)
canvasFish.create_oval(100,200,1000,350,fill="#DDA906")
canvasFish.create_oval(200,250,170,270,fill="black")
canvasFish.create_line(250,220,250,330)
canvasFish.create_polygon(990,275,1100,200,1100,350,fill="#F16831")
canvasFish.create_polygon(550,200,450,100,650,100,fill="#F16831")
canvasFish.create_polygon(550,350,450,450,650,450,fill="#F16831")
canvasFish.place(x=10,y=10)
