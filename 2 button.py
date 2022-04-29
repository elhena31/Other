from calendar import month
from cgitb import text
from doctest import master
from json.tool import main
from logging import root
from msilib.schema import Font
from tkinter import *
from tkinter import ttk
from turtle import bgcolor, left, update

class HelloApp:

    def __init__(self, master) -> None:
        sec = StringVar()
        Entry(master, textvariable=sec, width = 2, font = 'Helvetica 14').place(x=220, y=120)
        sec.set('00')
        self.label = ttk.Label(master, text = " Hello buddy!")
        self.label.config(foreground='red', background='yellow', font=('Calibri',18, 'bold'))
        self.label.grid(row=0, column=0, columnspan=2)

        ttk.Button(master, text='Soccer', command=self.clck_update).grid(row=3,column=0)
        ttk.Button(master, text='Close', command=self.close).grid(row=1, column=0)
        ttk.Combobox(master, textvariable=month).grid(row=4,column=0)
        ttk.Spinbox(master, from_=1990, to = 9999, textvariable = year, bgcolor='green').pack
        ttk.Button(master, text='Open', command=self.open).grid(row=2, column=0)
    
    def clck_update(self, master):
        sec = StringVar()
        Entry(master, textvariable=sec, width = 2, font = 'Helvetica 14').place(x=220, y=120)
        sec.set('00')
        mins= StringVar()
        Entry(master, textvariable = mins, width =2, font = 'Helvetica 14').place(x=180, y=120)
        mins.set('00')
        hrs= StringVar()
        Entry(master, textvariable = hrs, width =2, font = 'Helvetica 14').place(x=142, y=120)
        hrs.set('00')
        #Define the function for the timer
        
        def countdowntimer():
            times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
            while times > -1:
                minute,second = (times // 60 , times % 60)
                hour =0
                if minute > 60:
                    hour , minute = (minute // 60 , minute % 60)
                sec.set(second)
                mins.set(minute)
                hrs.set(hour)
                #Update the time
                master.update()
                time.sleep(1)
                if(times == 0):
                    sec.set('00')
                    mins.set('00')
                    hrs.set('00')
                times -= 1


    def soccer(self):
        self.label.config(text='field')
        


    def close(self):
        self.label.config(text='Closed')
        
    
    def open(self):
        self.label.config(text='Opened')
        

def main():

    root=Tk()
    root.geometry('750x300')
    Button(root, text='START', bd ='2', bg = 'IndianRed1',font =('Helveticabold',10), fg='green').place(x=167, y=165)
    app=HelloApp(root)
    root.mainloop()
if __name__=="__main__": main()