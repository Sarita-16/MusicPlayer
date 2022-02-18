import os  # to select the music mp3 files
import pickle
import tkinter as tk  # to create GUI(Graphical User Interface) for music application
from tkinter import *  # to select particular folder
from tkinter import PhotoImage  # to display images
from pygame import mixer  # to play, pause, control the volume of music
from PIL import ImageTk, Image      #to change jpg to gif


# Create a window using OOPs
class Player(tk.Frame):  # tk.Frame exactly same a root
    # to pass root window in this class
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.playlist = []  # create a empty list

        self.create_frames()
        self.track_widgets()
        self.control_widgets()

    # Create 3 frames in main window
    def create_frames(self):
        # To create a label frame for 1st frame
        self.track = tk.LabelFrame(self, text='Song Track',
                                   font=("Harlow solid italic", 20, "bold"),
                                   bg="blanched almond", fg="black", bd=5, relief=tk.GROOVE)
        self.track.configure(width=1010, height=400,bg = "lavenderblush2")  # configure it's size
        self.track.grid(row=0, column=0, padx=10)

        # To create a label frame for 2nd frame
        self.tracklist = tk.LabelFrame(self, text=f'Playlist - {str(len(self.playlist))}',
                                       font=("Harlow solid italic", 15, "bold"),
                                       bg="maroon", fg="white", bd=5, relief=tk.GROOVE)
        self.tracklist.configure(width=380, height=800)  # configure it's size
        self.tracklist.grid(row=0, column=1, rowspan=3, pady=5)

        # To create a label frame for 3rd frame
        self.controls = tk.LabelFrame(self,
                                      font=("Harlow solid italic", 15, "bold"),
                                      bg="blanched almond", fg="white", bd=2, relief=tk.GROOVE)
        self.controls.configure(width=1010, height=60,bg = "lavenderblush2")  # configure it's size
        self.controls.grid(row=1, column=0, pady=5, padx=10)

    #functions to display track image and functioning buttons
    def track_widgets(self):
        self.label = tk.Label(self.track,image = img)
        self.label.configure(width=1000, height=400)
        self.label.grid(row = 0,column = 0)

        self.label = tk.Label(self.track, font =("Harlow solid italic", 15, "bold"),
                               bg="blanched almond",fg="violetred4")
        self.label["text"] = "song name"
        self.label.configure(width=30, height=5)
        self.label.grid(row=1, column=0)
    def control_widgets(self):
        self.prev = tk.Button(self.controls, image=prev_)
        self.prev.grid(row=0, column=0)

        self.pause = tk.Button(self.controls, image=pause_)
        self.pause.grid(row=0, column=1)

        self.next = tk.Button(self.controls, image=next_)
        self.next.grid(row=0, column=2)

        self.volume = tk.DoubleVar()
        self.slider = tk.Scale(self.controls,
                                    from_ = 0, to = 10,
                                    orient = tk.HORIZONTAL ,
                                    resolution=.1)
        self.slider['variable'] = self.volume
        self.slider.set(5)
        self.slider.grid(row =0,column = 3 , padx= 5 , pady = 5 )
# Create a window
root = tk.Tk()
root.geometry('1050x600')  # to change the size of window
root.wm_title('Music Player')  # to change the title of window
# root.mainloop()       #to display in the main window

img = ImageTk.PhotoImage(Image.open("images/music_logo1.jpg"))  #we use imagetk and photoimage to change the jpg
                                                                # image into gif as tkinter does not support jpg
prev_= ImageTk.PhotoImage(Image.open("images/backward.jpg"))
next_= ImageTk.PhotoImage(Image.open("images/forward.jpg"))
play_= ImageTk.PhotoImage(Image.open("images/play.jpg"))
pause_= ImageTk.PhotoImage(Image.open("images/pause.jpg"))

root.configure(bg = "lavenderblush2")  #bgcolor of window
# to create a object in that class to see in main window
app = Player(master=root)  # object_name = class_name
app.mainloop()  # call the loop
