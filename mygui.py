from tkinter import *
import os
import subprocess

mygui = Tk()
mygui.geometry("1920x1080")
mygui.title("Planning Applications")
def execute():
    p = subprocess.Popen('python case.py',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output, errors = p.communicate()
    text = Text(mygui,bg="grey94",font=("Helvetica", 16))
    text.pack()
    text.place(x=500,y=400)
    text.insert(END, output)

w = Label(mygui,text="Planning Application Outcome Prediction",font=("Helvetica", 28, "bold"))
w.place(x=650,y=10)
    
B = Button(mygui, text = "Execute", command = execute,font=("Helvetica", 12))
B.place(x = 900,y = 250)
mygui.mainloop()