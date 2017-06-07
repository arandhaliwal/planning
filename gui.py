import tkinter as tk
from tkinter import *
from tkinter import font
import subprocess
from PIL import ImageTk, Image

ebonyclay =  '#42424d'
darkershade =  '#313139'
yellowwhite = '#fafaef'

gui = Tk()
gui.geometry("1920x1080")
gui.title("Planning Applications")
gui.configure(background=ebonyclay)

with open("addfactorslist.txt","r") as factors:
        factorslist = []
        for line in factors:
            factorslist.append(line)
        factorslist = [i.strip() for i in factorslist]
   
def reset(f1,frame,back):
    f1.destroy()
    back.destroy()
    frame.destroy()
    B = Button(gui, text = "Execute", command = lambda: execute(B,C,label1,text1,label2,text2,'normal',label3,label4,Lb1),font=("Open Sans Light", 12),bg=ebonyclay,fg = yellowwhite)
    B.place(x = 1550,y = 300)
    
    C = Button(gui, text = "Execute", command = lambda: execute(B,C,label1,text1,label2,text2,'fao',label3,label4,Lb1),font=("Open Sans Light", 12),bg=ebonyclay,fg = yellowwhite)
    C.place(x = 1550,y = 500)

    label1 = Label(gui,text = "Enter proposal:",font=("Open Sans Light", 14),bg=ebonyclay,fg = yellowwhite)
    label1.place(x=50,y = 250)

    text1 = Text(gui,height = 5,width = 100,bg = darkershade,fg = yellowwhite,font = ("Open Sans Light",12))
    text1.place(x = 250, y = 250)

    label2 = Label(gui,text = "Enter constraints:",font=("Open Sans Light", 14),bg=ebonyclay,fg = yellowwhite)
    label2.place(x=50,y = 450)

    text2 = Text(gui,height = 15,width = 100,bg = darkershade,fg = yellowwhite,font = ("Open Sans Light",12))
    text2.place(x = 250, y = 450)
    
    label3 = Label(gui,text = "Predict outcome",font=("Open Sans Light", 14),bg=ebonyclay,fg = yellowwhite)
    label3.place(x=1510,y = 250)

    label4 = Label(gui,text = "Predict whether something can be added",font=("Open Sans Light", 14),bg=ebonyclay,fg = yellowwhite)
    label4.place(x=1425,y = 450)
    
    Lb1 = Listbox(gui,height = 10,width = 20,bg = darkershade,fg = yellowwhite,font = ("Open Sans Light",12))
    i = 1
    for factor in factorslist:
        Lb1.insert(i,factor)
        i+=1
    Lb1.place(x = 1480, y = 600)
    
        
def retrieve_input1(text1):
    return text1.get("1.0","end-1c")

def retrieve_input2(text2):
    return text2.get("1.0","end-1c")

def retrieve_inputlb(Lb1):
    return Lb1.get(Lb1.curselection())
    
def execute(B,C,label1,text1,label2,text2,type,label3,label4,Lb1):
    f = open("proposalinput.txt","w+")
    f.write(retrieve_input1(text1))
    f.close()
    f = open("constraintsinput.txt","w+")
    f.write(retrieve_input2(text2))
    f.close()
    if type == 'normal':
        p = subprocess.Popen('python guiexecute.py',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if type == 'fao':
        f = open("factorinput.txt","w+")
        f.write(retrieve_inputlb(Lb1))
        f.close()
        p = subprocess.Popen('python guiexecutefao.py',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output, errors = p.communicate()
    B.destroy()
    C.destroy()
    label1.destroy()
    text1.destroy()
    label2.destroy()
    text2.destroy()
    label3.destroy()
    label4.destroy()
    Lb1.destroy()
    
    f1 = Frame(gui)
    f1.place(x=100,y=200)
    scrollbar = Scrollbar(f1)
    scrollbar.pack( side = RIGHT, fill = Y )
    text = Text(f1,font=("Open Sans Light", 16),bg=ebonyclay,fg = yellowwhite,bd=0,yscrollcommand = scrollbar.set,width=40,height=35)
    text.pack()
    text.insert(END, output)
    scrollbar.config( command = text.yview )
    
    frame = Frame(gui)
    frame.place(x=700,y=200)
    xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
    yscrollbar = Scrollbar(frame)
    xscrollbar.pack( side = BOTTOM, fill = X )
    yscrollbar.pack( side = RIGHT, fill = Y )
    canvas = Canvas(frame, bd=0, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set,width=1100,height=810)
    img = ImageTk.PhotoImage(Image.open("tree.png"))
    canvas.create_image(0,0,image=img)
    canvas.image = img
    xscrollbar.config(command=canvas.xview)
    yscrollbar.config(command=canvas.yview)
    canvas.config(scrollregion=canvas.bbox(ALL))
    canvas.pack()
    
    back = Button(gui, text = "Back", command = lambda: reset(f1,frame,back),font=("Open Sans Light", 12),bg=ebonyclay,fg = yellowwhite)
    back.place(x = 0,y = 0)
    

w = Label(gui,text="Planning Application Outcome Prediction",font=("Open Sans Light", 32),bg=ebonyclay,fg = yellowwhite)
w.place(x=500,y=75)
    
B = Button(gui, text = "Execute", command = lambda: execute(B,C,label1,text1,label2,text2,'normal',label3,label4,Lb1),font=("Open Sans Light", 12),bg=ebonyclay,fg = yellowwhite)
B.place(x = 1550,y = 300)

C = Button(gui, text = "Execute", command = lambda: execute(B,C,label1,text1,label2,text2,'fao',label3,label4,Lb1),font=("Open Sans Light", 12),bg=ebonyclay,fg = yellowwhite)
C.place(x = 1550,y = 500)


label1 = Label(gui,text = "Enter proposal:",font=("Open Sans Light", 14),bg=ebonyclay,fg = yellowwhite)
label1.place(x=50,y = 250)

text1 = Text(gui,height = 5,width = 100,bg = darkershade,fg = yellowwhite,font = ("Open Sans Light",12))
text1.place(x = 250, y = 250)

label2 = Label(gui,text = "Enter constraints:",font=("Open Sans Light", 14),bg=ebonyclay,fg = yellowwhite)
label2.place(x=50,y = 450)

text2 = Text(gui,height = 15,width = 100,bg = darkershade,fg = yellowwhite,font = ("Open Sans Light",12))
text2.place(x = 250, y = 450)

label3 = Label(gui,text = "Predict outcome",font=("Open Sans Light", 14),bg=ebonyclay,fg = yellowwhite)
label3.place(x=1510,y = 250)

label4 = Label(gui,text = "Predict if something can be added",font=("Open Sans Light", 14),bg=ebonyclay,fg = yellowwhite)
label4.place(x=1425,y = 450)

Lb1 = Listbox(gui,height = 10,width = 20,bg = darkershade,fg = yellowwhite,font = ("Open Sans Light",12))
i = 1
for factor in factorslist:
    Lb1.insert(i,factor)
    i+=1
Lb1.place(x = 1480, y = 600)


gui.mainloop()