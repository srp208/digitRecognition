from tkinter import *
from tensorflowTesting import testing
##import tensorflow as tf
from keras.models import load_model
import cv2
import numpy as np
import os

from PIL import ImageTk, Image, ImageDraw
import PIL
import tkinter as tk
from tkinter import *

classes=[0,1,2,3,4,5,6,7,8,9]
width = 450
height = 450
center = height//2
white = (255, 255, 255)
green = (0,128,0)

def paint(event):
    x1, y1 = (event.x - 10), (event.y - 10)
    x2, y2 = (event.x + 10), (event.y + 10)
    cv.create_oval(x1, y1, x2, y2, fill="black",width=40)
    draw.line([x1, y1, x2, y2],fill="black",width=40)
def model():
    filename = "image.png"
    image1.save(filename)
    pred=testing()
    print('argmax',np.argmax(pred[0]),'\n',
          pred[0][np.argmax(pred[0])],'\n',classes[np.argmax(pred[0])])
    txt.insert(tk.INSERT,"Predicted Value: {}\nAccuracy: {}%".format(classes[np.argmax(pred[0])],round(pred[0][np.argmax(pred[0])]*100,3)))
    
def clear():
    cv.delete('all')
    draw.rectangle((0, 0, 500, 500), fill=(255, 255, 255, 0))
    txt.delete('1.0', END)

root = Tk()
root.geometry('900x700') 
root.config(bg="red", borderwidth=3, relief=SUNKEN)

cv = Canvas(root, width=width, height=height, bg='light blue',relief=SOLID ,  borderwidth=4)
cv.pack()

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = PIL.Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

txt=tk.Text(root,bd=3,exportselection=0,bg='pink',font=('Helvetica bold',20),
            padx=10,pady=10,height=5,width=25,borderwidth=5,relief=SOLID)

cv.pack(expand=YES, fill=BOTH)
cv.bind("<B1-Motion>", paint)


btnModel=Button(text="PREDICT DIGIT",font=('Times New Roman bold',12),height=2,width=20,fg="black",bg="yellow",borderwidth=5,relief=SOLID,command=model)
btnClear=Button(text="CLEAR",font=('Times New Roman bold',12),height=2,width=20,bg="yellow",fg="black",borderwidth=5,relief=SOLID,command=clear)
##button.pack()
btnModel.pack(pady=7)
btnClear.pack(pady=7)
# button_border.pack()
txt.pack()
root.title('DIGIT RECOGNIZER')
root.mainloop()
