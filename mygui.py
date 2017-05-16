from tkinter import *
import subprocess

mygui = Tk()
mygui.geometry("1920x1080")
mygui.title("Planning Applications")
def execute():
    p = subprocess.Popen('python case.py',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output, errors = p.communicate()
    text = Text(mygui,bg="grey94",font=("Helvetica", 16))
    text.pack()
    text.place(x=500,y=450)
    text.insert(END, output)

w = Label(mygui,text="Planning Application Outcome Prediction",font=("Helvetica", 28, "bold"))
w.place(x=600,y=10)
    
B = Button(mygui, text = "Execute", command = execute,font=("Helvetica", 12))
B.place(x = 1500,y = 225)


label1 = Label(mygui,text = "Enter proposal:",font=("Helvetica", 14))
label1.place(x=0,y = 100)

text1 = Text(mygui,height = 5,width = 100)
text1.place(x = 200, y = 100)

label2 = Label(mygui,text = "Enter constraints:",font=("Helvetica", 14))
label2.place(x=0,y = 300)

text1 = Text(mygui,height = 5,width = 100)
text1.place(x = 200, y = 300)

mygui.mainloop()