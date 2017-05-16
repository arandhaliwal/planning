from tkinter import *
import os
import subprocess

mygui = Tk()
mygui.geometry("750x500")
mygui.title("Planning Applications")
def execute():
    p = subprocess.Popen('python case.py',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output, errors = p.communicate()
    text = Text(mygui)
    text.pack()
    text.insert(END, output)

B = Button(mygui, text = "Execute", command = execute)
B.place(x = 325,y = 250)
mygui.mainloop()
