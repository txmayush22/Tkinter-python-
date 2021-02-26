from tkinter import *
root=Tk()


root.geometry("1450x700+0+0")
canvas=Canvas(root,background="white",width=1200,height=700)


#sun
canvas.create_oval(400,200,700,500,fill="#F3C310")
canvas.create_line(225,0,900,650,fill="#F3C310")
canvas.create_line(250,650,900,0,fill="#F3C310")
canvas.create_line(550,0,550,750,fill="#F3C310")
canvas.create_line(100,350,1000,350,fill="#F3C310")

canvas.place(x=10,y=10)
