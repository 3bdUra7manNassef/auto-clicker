
#todo (the root),(the func for btns),(add all buttons)
#*modules*#
from tkinter import *
import time 
import pyautogui

#!root of program!#
root = Tk()
root.title('auto clicker by 3bdo')
root.geometry('150x150')

#*func for button*#
def click ():
    time.sleep(5)
    while True:
        pyautogui.doubleClick()

def dclick ():
    time.sleep(5)
    while True:
        pyautogui.tripleClick()

def tclick ():
    time.sleep(5)
    while True:
        pyautogui.click()

#?the buttons?#
btn_click = Button(root,command=click,text='(1)click')
btn_doubleClick = Button(root,command=dclick,text='doubleClick')
btn_tripleClick = Button(root,command=tclick,text='tripleClick')

btn_click.pack()
btn_tripleClick.pack()
btn_doubleClick.pack()
mainloop()