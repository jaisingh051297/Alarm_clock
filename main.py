"""
   This is GUI base Alarm clock. In this clock, We can setup Alarm and able to see Current time.
"""



from tkinter import *  #tkinter is python package use for  GUI (Graphical User Interface) designing.
import datetime
from tkinter import messagebox # this tkinter module is used for showing massage on screen
import threading #  this Python Module used in cases where the execution of a task involves some waiting time.
import time  # it is user for taking current time.
from pygame import mixer  # this python module used to give sound effect.


class Clock:


    def __init__(self,win):
        '''
        It is use for creating dimensions of GUI window screen such
        as screen size, colour of screen ,input field,button ,labels and
        many more .
        win: It is our main GUI window screen object
        '''


        self.win = win
        self.win.geometry("530x330")  # used for screen Size
        self.win.title("Alarm_Clock")  # use to give Title


        mixer.init()  # Mixer used to give sound effect

        def ala():  # Used to provide some waiting time.
            t = threading.Thread(target=a, args=())

            t.start()

        def a():

            a = f"{altime.get()}" # used to fetching the data in "HH:MM"
            if a == "":
                msg = messagebox.showerror('Invalid data', 'Please enter valid time') # used to so error if user does not enter any value.
            else:
                AlarmT = a
                CurrentTime = time.strftime("%H:%M")  # used to fetching current time "HH:MM"

                while AlarmT != CurrentTime:
                    CurrentTime = time.strftime("%H:%M") # used to up-date current time.

                if AlarmT == CurrentTime: # condition to check Alarm time with current time.
                    mixer.music.load('alarm_beeps.mp3')  # used to load music tone.
                    mixer.music.play()  # used to Play music tone.




        self.win.config(bg="pink")  # background colour
        self.head = Label(self.win, text="Alarm Clock", font=("times new roman", 20),padx=30,pady=15)  # it used to give Heading.
        self.head.grid(row=0, columnspan=5)  # Used to locate Text position on screen.


        self.msg = Label(self.win, text=" Enter Alarm time \n(Hr:Min)",font=("times new roman", 18),bg="green",padx=14,pady=8) # printing some text on screen.
        self.msg.grid(row=2,columnspan=5)  # It is used to locate text position on screen.

        self.inputt = Label(self.win, text="Input time", font=("times new roman", 18))  # printing some text on screen.
        self.inputt.grid(row=3, column=0)  # It is used to locate text position.

        altime = Entry(self.win, font=("times new roman", 18), width=6) # used for Taking input
        altime.grid(row=3, column=1) # It is used to locate data input field position.

        self.submit = Button(self.win, text="SUBMIT", font=("times new roman", 18),padx=10,pady=8, command=ala)  # It is used for making Button
        self.submit.grid(row=7, columnspan=2) # It is used to locate Button position.







win = Tk() # Used to create tkinter window
clock_obj = Clock(win) # creating an object
win.mainloop() # ending of tkinter program
