from cgitb import text
from json.tool import main
from logging import root
from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master) -> None:
        self.label = ttk.Label(master, text = " Hello buddy!")
        self.label.grid(row=0, column=0, columnspan=2)

        ttk.Button(master, text='Texas', command=self.texas_hello).grid(row=1, column=0)
        
        ttk.Button(master, text='Hawaii', command=self.hawaii_hello).grid(row=2, column=0)
    
    def texas_hello(self):
        self.label.config(text='Howdy cowboy!')
    
    def hawaii_hello(self):
        self.label.config(text='Aloha bali!')

def main():

    root=Tk()
    app=HelloApp(root)
    root.mainloop()
if __name__=="__main__": main()