from tkinter import *
root=Tk()

root.geometry("1450x700+0+0")
canvas=Canvas(root,background="white",width=1200,height=700)

#SMILEY

canvas.create_oval(200,50,800,650,fill="#F3C310")
canvas.create_oval(330,170,400,320,fill="black")
canvas.create_oval(580,170,650,320,fill="black")
canvas.create_arc(350, 350, 650, 550,start=0,extent=-180,fill="#E30505")

canvas.place(x=10,y=10)
