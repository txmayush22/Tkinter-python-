#flag
from tkinter import *
root=Tk()


root.geometry("1450x700+0+0")
canvas=Canvas(root,background="white",width=1200,height=700)


canvasFlag=Canvas(root,background="white",width=1200,height=700)
canvasFlag.create_rectangle(50,50,70,650,fill="brown")
canvasFlag.create_rectangle(71,50,350,100,fill="orange")
canvasFlag.create_rectangle(71,101,350,151,fill="white")
canvasFlag.create_rectangle(71,152,350,202,fill="green")
canvasFlag.create_oval(190,101,230,151)
canvasFlag.create_line(210,101,210,151,fill="blue")
canvasFlag.create_line(190,126,230,126,fill="blue")
canvasFlag.create_line(195,110,225,141,fill="blue")
canvasFlag.create_line(195,141,225,110,fill="blue")

canvasFlag.place(x=10,y=10)
