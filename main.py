import mysql.connector
import os
import tkinter as tk
from tkinter import ttk

# sql connection after initialization
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.environ['PASSWORD'],
    database="FriendsManager"
)
cursor = db.cursor()


# GUI / Main functionalities

# constants
FONT = ("Verdana", 30)
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500


# pages manager
class FriendsManager(tk.Tk):
    # init for friends_manager
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating container
        container = tk.Frame(self, height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
        container.pack(side="top", fill="both", expand=True)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple containing different page layouts
        for pages in (StartPage, CreatePage, ReadPage, UpdatePage, DeletePage):
            frame = pages(container, self)

            # putting the pages into the frames array
            self.frames[pages] = frame

            frame.place(relx=0, rely=0)

        # initialize start page
        self.show_frame(StartPage)

    # display the given frame
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# starting page
class StartPage(tk.Frame):
    # init function for the starting page
    def __init__(self, parent, controller):
        # initialize the class as a tkinter Frame
        tk.Frame.__init__(self, parent, height=SCREEN_HEIGHT, width=SCREEN_WIDTH)

        # starting page design
        label = ttk.Label(self, text="Choose an option", font=FONT)
        create_button = ttk.Button(self, text="Create a friend", command=lambda: controller.show_frame(CreatePage))
        read_button = ttk.Button(self, text="View a friend", command=lambda: controller.show_frame(ReadPage))
        update_button = ttk.Button(self, text="Update a friend", command=lambda: controller.show_frame(UpdatePage))
        delete_button = ttk.Button(self, text="Delete a friend", command=lambda: controller.show_frame(DeletePage))

        label.place(anchor=tk.CENTER, relx=0.5, rely=0.2)
        create_button.place(anchor=tk.CENTER, relx=0.5, rely=0.35)
        read_button.place(anchor=tk.CENTER, relx=0.5, rely=0.5)
        update_button.place(anchor=tk.CENTER, relx=0.5, rely=0.65)
        delete_button.place(anchor=tk.CENTER, relx=0.5, rely=0.80)


# create page
class CreatePage(tk.Frame):
    # init function for the starting page
    def __init__(self, parent, controller):
        # initialize the class as a tkinter Frame
        tk.Frame.__init__(self, parent, height=SCREEN_HEIGHT, width=SCREEN_WIDTH)

        # starting page design
        label = ttk.Label(self, text="Create a friend", font=FONT)
        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))

        label.place(anchor=tk.CENTER, relx=0.5, rely=0.2)
        back_button.place(anchor=tk.CENTER, relx=0.5, rely=0.8)


# read page
class ReadPage(tk.Frame):
    # init function for the starting page
    def __init__(self, parent, controller):
        # initialize the class as a tkinter Frame
        tk.Frame.__init__(self, parent, height=SCREEN_HEIGHT, width=SCREEN_WIDTH)

        # starting page design
        label = ttk.Label(self, text="View a friend", font=FONT)
        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))

        label.place(anchor=tk.CENTER, relx=0.5, rely=0.2)
        back_button.place(anchor=tk.CENTER, relx=0.5, rely=0.8)


# updating page
class UpdatePage(tk.Frame):
    # init function for the starting page
    def __init__(self, parent, controller):
        # initialize the class as a tkinter Frame
        tk.Frame.__init__(self, parent, height=SCREEN_HEIGHT, width=SCREEN_WIDTH)

        # starting page design
        label = ttk.Label(self, text="Update a friend", font=FONT)
        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))

        label.place(anchor=tk.CENTER, relx=0.5, rely=0.2)
        back_button.place(anchor=tk.CENTER, relx=0.5, rely=0.8)


# delete page
class DeletePage(tk.Frame):
    # init function for the starting page
    def __init__(self, parent, controller):
        # initialize the class as a tkinter Frame
        tk.Frame.__init__(self, parent, height=SCREEN_HEIGHT, width=SCREEN_WIDTH)

        # starting page design
        label = ttk.Label(self, text="Delete a friend", font=FONT)
        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))

        label.place(anchor=tk.CENTER, relx=0.5, rely=0.2)
        back_button.place(anchor=tk.CENTER, relx=0.5, rely=0.8)


screen = FriendsManager()
screen.mainloop()
