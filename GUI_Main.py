# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:27:05 2021

@author: om
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from tkvideo import tkvideo
'''import detection_emotion_practice as validate'''
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="#D15FEE")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("skin disease")

# 43
# video_label =tk.Label(root)
# video_label.pack()
# # read video to display on label
# player = tkvideo("Heart Beats - 4360.mp4", video_label,loop = 1, size = (w, h))
# player.play()
# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('a1.webp')
image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)


image2 = Image.open('a.JPG')
image2 = image2.resize((620, 500), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=80, y=170)  


#
image2 = Image.open('a3.jpg')
image2 = image2.resize((580, 500), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=700, y=170)  


# label_l1 = tk.Label(root, text="Keyboard and Mouse Detection System",font=("Times New Roman", 35, 'bold'),
#                     background="#FFEBCD", fg="black", width=50, height=1)
# label_l1.place(x=0, y=0)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)

label_l1 = tk.Label(root, text="Welcome to my Application",font=("Algerian", 25, 'bold'),
                    background="#FFEBCD", fg="#A70D2A", width=60, height=1)
label_l1.place(x=80, y=0)
#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)

canvas=tk.Canvas(root,bg="#FFC0CB")
canvas.pack()
canvas.place(x=0, y=50)
text_var="skin disease"
text=canvas.create_text(0,-2000,text=text_var,font=('Algerian',25,'bold'),fill='#3F9B0B',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = 1600
height = 90
canvas['width']=width
canvas['height']=height
fps=40    #Change the fps to make the animation faster/slower
shift()   #Function Calling

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#iframesrc = ("https://assets.pinterest.com/ext/embed.html?id=578853358377785481", height="1167", width="600" , frameborder="0", scrolling="no" )





# def cap_video():
    
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])

def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
    
 
    
def window():
  root.destroy()


button1 = tk.Button(root, text="LOGIN", command=log, width=12, height=1,font=('times', 20, ' bold '), bg="#FFEBCD", fg="#8FB31D")
button1.place(x=600, y=200)

button2 = tk.Button(root, text="REGISTER",command=reg,width=12, height=1,font=('times', 20, ' bold '), bg="#FFEBCD", fg="#8FB31D")
button2.place(x=600, y=270)

button3 = tk.Button(root, text="EXIT",command=window,width=12, height=1,font=('times', 20, ' bold '), bg="#FFEBCD", fg="brown")
button3.place(x=600, y=340)

root.mainloop()