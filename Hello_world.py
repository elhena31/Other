from os import times
from tkinter import *
import time
from tkinter.tix import COLUMN
from tracemalloc import stop
from PIL import ImageTk, Image
import random

#Create an instance of tkinter frame
window1 = Tk()
window1.geometry('750x600')
window1.resizable(True,True)

#Configure the background
window1.config(bg='blue')

#printing the image
icon1 = ImageTk.PhotoImage(Image.open
("/Users/sebastian.henao/Downloads/Python/Soccerfield.PNG"))
imglabel = Label(window1, image = icon1).grid(row=2, column = 2)

#Create Entry Widgets for HH MM SS
sec = StringVar()
Entry(window1, textvariable=sec, width = 2, font = 'Helvetica 14').place(x=225, y=500)
sec.set('00')
mins= StringVar()
Entry(window1, textvariable = mins, width =2, font = 'Helvetica 14').place(x=180, y=500)
mins.set('00')
cuotas = [1,2,3,4,5,6]
cuota_actual = random.choice(cuotas)
Entry(window1, textvariable = cuota_actual, width = 4, font = 'Helvetica 14').place(x=265, y=500)

#Define the function for the timer
def countdowntimer():
   times = int(mins.get())*60 + int(sec.get())
   while times > -1:
      minute,second = (times // 60 , times % 60)
      
      if minute > 60:
         minute = (minute // 60 , minute % 60)
      sec.set(second)
      mins.set(minute)

      #Update the time
      window1.update()
      time.sleep(1)
      if(times == 0):
         sec.set('00')
         mins.set('00')
      times -= 1
def timestop():
   window1.update()
   time.sleep(10)
   
Label(window1, font =('Helvetica bold',15), text = 'Set Timer',bg ='burlywood').place(x=70,y=500)
Button(window1, text='START', bd ='2', bg = 'IndianRed',font =('Helveticabold',10),
command = countdowntimer).place(x=100, y=565)
Button(window1, text='STOP', command=timestop).place(x=170, y=565)
#img = Image.open(r"C:\Users\sebastian.henao\Downloads\Python\Soccerfield1.gif")
window1.mainloop()