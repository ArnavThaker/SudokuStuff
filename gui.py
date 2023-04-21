from tkinter import *

from datetime import date, datetime

def guiTest():
    window = Tk()
    window.geometry("400x400")
    greeting = Label(text="Hello World")
    greeting.grid()
    window.mainloop()

if __name__ == "__main__":
    guiTest()