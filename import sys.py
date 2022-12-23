import sys
import os
from tkinter import *
window=Tk()
window.title("Running Python Script")
window.geometry('550x200')
def run():
    os.system("C:/Users/DYLAN/OneDrive/Desktop/human-activity-recognition-master/test/piano.mp4")
btn = Button(window, text="Video1", bg="black", fg="white",command=run)
btn.grid(column=0, row=0)
def run1():
    os.system("C:/Users/DYLAN/OneDrive/Desktop/human-activity-recognition-master/test/Crying.mp4")
btn1 = Button(window, text="Video2", bg="red", fg="white",command=run1)
btn1.grid(column=20, row=0)
def run2():
    os.system("C:/Users/DYLAN/OneDrive/Desktop/human-activity-recognition-master/test/Board - 60109.mp4")
19
btn2 = Button(window, text="Video3", bg="blue", fg="white",command=run2)
btn2.grid(column=30, row=0)
window.mainloop()