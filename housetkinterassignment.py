from tkinter import *
root=Tk()


root.geometry("1450x700+0+0")
canvas=Canvas(root,background="white",width=1200,height=700)


#FLAG
canvas.create_rectangle(400,350,900,680,fill="#EAB731")
canvas.create_polygon(650,50,900,350,400,350,fill="#651C17")
canvas.create_rectangle(450,400,550,500,fill="#2DE7D3")
canvas.create_rectangle(750,400,850,500,fill="#2DE7D3")
canvas.create_rectangle(600,550,700,680,fill="#8F39F0")

canvas.place(x=10,y=10)


