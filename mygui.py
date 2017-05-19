from tkinter import *
from tkinter import font
import subprocess
import os

ebonyclay =  '#42424d'
darkershade =  '#313139'
yellowwhite = '#fafaef'

mygui = Tk()
mygui.geometry("1920x1080")
mygui.title("Planning Applications")
mygui.configure(background=ebonyclay)
   
def reset(text,back):
    text.destroy()
    back.destroy()
    B = Button(mygui, text = "Execute", command = lambda: execute(B,label1,text1,label2,text2),font=("Open Sans Light", 12),bg=ebonyclay,fg = yellowwhite)
    B.place(x = 1550,y = 390)

    label1 = Label(mygui,text = "Enter proposal:",font=("Open Sans Light", 14),bg=ebonyclay,fg = yellowwhite)
    label1.place(x=50,y = 250)

    text1 = Text(mygui,height = 5,width = 100,bg = darkershade,fg = yellowwhite,font = ("Open Sans Light",12))
    text1.place(x = 250, y = 250)

    label2 = Label(mygui,text = "Enter constraints:",font=("Open Sans Light", 14),bg=ebonyclay,fg = yellowwhite)
    label2.place(x=50,y = 450)

    text2 = Text(mygui,height = 15,width = 100,bg = darkershade,fg = yellowwhite,font = ("Open Sans Light",12))
    text2.place(x = 250, y = 450)
        
def retrieve_input1():
    return text1.get("1.0","end-1c")

def retrieve_input2():
    return text2.get("1.0","end-1c")    
    
def execute(B,label1,text1,label2,text2):
    f = open("test1.txt","w+")
    f.write(retrieve_input1())
    f.close()
    f = open("test2.txt","w+")
    f.write(retrieve_input2())
    f.close()
    p = subprocess.Popen('python case.py',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output, errors = p.communicate()
    B.destroy()
    label1.destroy()
    text1.destroy()
    label2.destroy()
    text2.destroy()
    text = Text(mygui,font=("Open Sans Light", 18),bg=ebonyclay,fg = yellowwhite,bd=0)
    text.pack()
    text.place(x=500,y=250)
    text.insert(END, output)
    back = Button(mygui, text = "Back", command = lambda: reset(text,back),font=("Open Sans Light", 12),bg=ebonyclay,fg = yellowwhite)
    back.place(x = 0,y = 0)

w = Label(mygui,text="Planning Application Outcome Prediction",font=("Open Sans Light", 32),bg=ebonyclay,fg = yellowwhite)
w.place(x=500,y=75)
    
B = Button(mygui, text = "Execute", command = lambda: execute(B,label1,text1,label2,text2),font=("Open Sans Light", 12),bg=ebonyclay,fg = yellowwhite)
B.place(x = 1550,y = 390)


label1 = Label(mygui,text = "Enter proposal:",font=("Open Sans Light", 14),bg=ebonyclay,fg = yellowwhite)
label1.place(x=50,y = 250)

text1 = Text(mygui,height = 5,width = 100,bg = darkershade,fg = yellowwhite,font = ("Open Sans Light",12))
text1.place(x = 250, y = 250)

label2 = Label(mygui,text = "Enter constraints:",font=("Open Sans Light", 14),bg=ebonyclay,fg = yellowwhite)
label2.place(x=50,y = 450)

text2 = Text(mygui,height = 15,width = 100,bg = darkershade,fg = yellowwhite,font = ("Open Sans Light",12))
text2.place(x = 250, y = 450)

mygui.mainloop()