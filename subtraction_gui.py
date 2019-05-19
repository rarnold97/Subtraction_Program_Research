# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk

import numpy as np 


gui = tk.Tk()
#add widgets here 
gui.title('Blue Light Subtraction Program Pannel')

close_button = tk.Button(gui, text='Close', width=25, command = gui.destroy,activebackground='blue')
close_button.grid(row=1,column =2)

tk.Label(gui,text='Filename:').grid(row=0)
file_box = tk.Entry(gui, width=100)
file_box.grid(row=0,column=1)


gui.mainloop();
