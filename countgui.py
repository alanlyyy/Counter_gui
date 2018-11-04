"""
A gui counter app
The user clicks on the button which will update a counter and display it to the user

"""
from tkinter import *
#import all objects from tkinter library

import time
import datetime

window = Tk()
#create a tkinter object 

#create a integer variable to be stored in tkinter object
counter= IntVar()

#start the count at 0
counter.set(0)

def count_up():
	#when method is invoked, get the current count and add 1 to it.
	#set to tkinter IntVar()
	counter.set(counter.get() + 1)

def count_down():
	#when method is invoked, get the current count and add 1 to it.
	#set to tkinter IntVar()
	counter.set(counter.get() - 1)

def time_refresh():
	#refreshes time on screen when pressed
	current_time.set(datetime.datetime.now().time())



#create a button window, when press invoke count_up method
b1 = Button(window,text="increment",command=count_up)
b1.grid(row=1,column=0)

b2 = Button(window,text="decrement", command=count_down)
b2.grid(row=1,column=1)

#create a label to hold the value of the counter
count_hold = Label(window, textvariable=counter)
count_hold.grid(row=2,column=1)

b3 = Button(window,text="time refresh", command= time_refresh)
b3.grid(row=1,column=2)

current_time = StringVar()
current_time.set(datetime.datetime.now().time())

current_time_hold = Label(window, textvariable=current_time)
current_time_hold.grid(row=0,column=0)

window.mainloop()