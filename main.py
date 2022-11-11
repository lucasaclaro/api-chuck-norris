import requests
import tkinter
from tkinter import *

link = 'https://api.chucknorris.io/jokes/random'
request = requests.get(link)
request_json = request.json()
text = request_json.get('value')

master = Tk()
master.title('The legend')
master.geometry('1400x800+250+100')
master.minsize(1400, 800)
master.maxsize(1400, 800)
background = PhotoImage(file='images/background.png')
background_master = Label(master, image=background)
background_master.pack()



title = Label(master, text='Chuck Norris, the legend', font=('Verdana', 18, 'bold'), fg='white', background='black')
title.place(width=345, height=50, x=540, y=10)

def btn_click():
    result = Label(master, text=text, font=('Verdana', 10, 'bold'), fg='white', background='black')
    result.place(width=1400, height=30, x=10, y=200)

    button_close = Button(master, text='Close window', font=('Verdana', 18, 'bold'), command=master.destroy)
    button_close.place(width=260, height=30, x=600, y=400)



button = Button(master, text='Click here', font=('Verdana', 18, 'bold'), command=btn_click)
button.place(width=280, height=30, x=580, y=100)













master.mainloop()