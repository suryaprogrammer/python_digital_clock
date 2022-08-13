from re import X
import time
import tkinter
from tkinter import font
from turtle import bgcolor
import pyglet
pyglet.font.add_file('digital-7.ttf')
root = tkinter.Tk()


def update_time():
   
    print(time.ctime())
    timming.config(text=time.ctime())
    timming.after(1000,update_time)








root.title("Digital clock")
root.geometry("855x90")

timming = tkinter.Label(root,bg="black",fg="green",font="digital-7 66 bold",padx=20)
timming.pack(fill="both")
update_time()
root.mainloop()



