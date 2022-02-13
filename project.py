import os  # to select the music mp3 files
import pickle
import tkinter as tk  # to create GUI(Graphical User Interface) for music application
from tkinter import filedialog  # to select particular folder
from tkinter import PhotoImage  # to display images
from pygame import mixer  # to play, pause, control the volume of music


# Create a window using OOPs
class Player(tk.Frame):  # tk.Frame exactly same a root
    # to pass root window in this class
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.playlist = []  # create a empty list

        self.create_frames()

    # Create 3 frames in main window
    def create_frames(self):
        # To create a label frame for 1st frame
        self.track = tk.LabelFrame(self, text='Song Track',
                                   font=("times new roman", 15, "bold"),
                                   bg="grey", fg="white", bd=5, relief=tk.GROOVE)
        self.track.configure(width=600, height=390)  # configure it's size
        self.track.grid(row=0, column=0, padx=10)

        # To create a label frame for 2nd frame
        self.tracklist = tk.LabelFrame(self, text=f'Playlist - {str(len(self.playlist))}',
                                       font=("times new roman", 15, "bold"),
                                       bg="black", fg="white", bd=5, relief=tk.GROOVE)
        self.tracklist.configure(width=380, height=680)  # configure it's size
        self.tracklist.grid(row=0, column=1, rowspan=3, pady=5)

        # To create a label frame for 3rd frame
        self.controls = tk.LabelFrame(self,
                                      font=("times new roman", 15, "bold"),
                                      bg="white", fg="white", bd=2, relief=tk.GROOVE)
        self.controls.configure(width=600, height=290)  # configure it's size
        self.controls.grid(row=2, column=0, pady=5, padx=10)


# Create a window
root = tk.Tk()
root.geometry('800x600')  # to change the size of window
root.wm_title('Music Player')  # to change the title of window
# root.mainloop()       #to display in the main window

# to create a object in that class to see in main window
app = Player(master=root)  # object_name = class_name
app.mainloop()  # call the loop
