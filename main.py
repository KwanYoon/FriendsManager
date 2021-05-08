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
LABELFONT = ("Verdana", 20)
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800


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

        # function
        def submit_create():
            cursor.execute("INSERT INTO Friends (first_name, last_name, birthday, likes, dislikes, additional)"
                           "VALUES (%s,%s,%s,%s,%s,%s)", (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get()))
            db.commit()
            e1.delete(0, tk.END)
            e2.delete(0, tk.END)
            e3.delete(0, tk.END)
            e4.delete(0, tk.END)
            e5.delete(0, tk.END)
            e6.delete(0, tk.END)

        # starting page design
        label = ttk.Label(self, text="Create a friend", font=FONT)

        tk.Label(self, text="First Name", font=LABELFONT).place(anchor=tk.CENTER, relx=0.3, rely=0.2)
        tk.Label(self, text="Last Name", font=LABELFONT).place(anchor=tk.CENTER, relx=0.3, rely=0.3)
        tk.Label(self, text="Birthday", font=LABELFONT).place(anchor=tk.CENTER, relx=0.3, rely=0.4)
        tk.Label(self, text="Likes", font=LABELFONT).place(anchor=tk.CENTER, relx=0.3, rely=0.5)
        tk.Label(self, text="Dislikes", font=LABELFONT).place(anchor=tk.CENTER, relx=0.3, rely=0.6)
        tk.Label(self, text="Additional", font=LABELFONT).place(anchor=tk.CENTER, relx=0.3, rely=0.7)

        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        e3 = tk.Entry(self)
        e4 = tk.Entry(self)
        e5 = tk.Entry(self)
        e6 = tk.Entry(self)

        submit_button = ttk.Button(self, text="Submit", command=submit_create)
        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))

        label.place(anchor=tk.CENTER, relx=0.5, rely=0.1)
        e1.place(anchor=tk.CENTER, relx=0.7, rely=0.2)
        e2.place(anchor=tk.CENTER, relx=0.7, rely=0.3)
        e3.place(anchor=tk.CENTER, relx=0.7, rely=0.4)
        e4.place(anchor=tk.CENTER, relx=0.7, rely=0.5)
        e5.place(anchor=tk.CENTER, relx=0.7, rely=0.6)
        e6.place(anchor=tk.CENTER, relx=0.7, rely=0.7)
        submit_button.place(anchor=tk.CENTER, relx=0.3, rely=0.9)
        back_button.place(anchor=tk.CENTER, relx=0.7, rely=0.9)


# read page
class ReadPage(tk.Frame):
    # init function for the starting page
    def __init__(self, parent, controller):
        # initialize the class as a tkinter Frame
        tk.Frame.__init__(self, parent, height=SCREEN_HEIGHT, width=SCREEN_WIDTH)

        # function
        def submit_read():
            if not e1.get() and not e2.get():
                cursor.execute("SELECT * FROM Friends")
            elif not e1.get():
                cursor.execute("SELECT * FROM Friends WHERE last_name=%s", (e2.get(),))
            elif not e2.get():
                cursor.execute("SELECT * FROM Friends WHERE first_name=%s", (e1.get(),))
            else:
                cursor.execute("SELECT * FROM Friends WHERE first_name=%s AND last_name=%s", (e1.get(), e2.get(),))

            text = ""
            for friend in cursor:
                text += "ID: " + str(friend[0]) + ", Name: " + friend[1] + " " + friend[2] + ", " + "Birthday: " + \
                        friend[3] + ", " + "Likes: " + friend[4] + ", " + "Dislikes: " + friend[5] + \
                        " Additional: " + friend[6] + "\n\n"
            if len(text) == 0:
                text += "There are no friends in the database with that name"
            friends_label_text.set(text)

        # starting page design
        label = ttk.Label(self, text="View a friend", font=FONT)

        tk.Label(self, text="First Name", font=LABELFONT).place(anchor=tk.CENTER, relx=0.3, rely=0.2)
        friends_label_text = tk.StringVar(value="")
        tk.Label(self, textvariable=friends_label_text).place(anchor=tk.CENTER, relx=0.5, rely=0.5)
        tk.Label(self, text="Last Name", font=LABELFONT).place(anchor=tk.CENTER, relx=0.3, rely=0.3)

        e1 = tk.Entry(self)
        e2 = tk.Entry(self)

        submit_button = ttk.Button(self, text="Submit", command=submit_read)
        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))

        label.place(anchor=tk.CENTER, relx=0.5, rely=0.1)
        e1.place(anchor=tk.CENTER, relx=0.7, rely=0.2)
        e2.place(anchor=tk.CENTER, relx=0.7, rely=0.3)
        submit_button.place(anchor=tk.CENTER, relx=0.3, rely=0.9)
        back_button.place(anchor=tk.CENTER, relx=0.7, rely=0.9)


# updating page
class UpdatePage(tk.Frame):
    # init function for the starting page
    def __init__(self, parent, controller):
        # initialize the class as a tkinter Frame
        tk.Frame.__init__(self, parent, height=SCREEN_HEIGHT, width=SCREEN_WIDTH)

        # functions
        def submit_search():
            cursor.execute("SELECT * FROM Friends WHERE id=%s", (e0.get(),))
            for friend in cursor:
                e1.insert(0, friend[1])
                e2.insert(0, friend[2])
                e3.insert(0, friend[3])
                e4.insert(0, friend[4])
                e5.insert(0, friend[5])
                e6.insert(0, friend[6])

        def submit_update():
            cursor.execute("UPDATE Friends SET first_name=%s, last_name=%s, birthday=%s, likes=%s, dislikes=%s, "
                           "additional=%s WHERE id=%s",
                           (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e0.get()))
            db.commit()
            e0.delete(0, tk.END)
            e1.delete(0, tk.END)
            e2.delete(0, tk.END)
            e3.delete(0, tk.END)
            e4.delete(0, tk.END)
            e5.delete(0, tk.END)
            e6.delete(0, tk.END)

        # starting page design
        label = ttk.Label(self, text="Update a friend", font=FONT)

        tk.Label(self, text="ID of friend to update", font=LABELFONT).place(anchor=tk.CENTER, relx=0.3, rely=0.2)
        search_button = ttk.Button(self, text="Search for ID", command=submit_search)
        tk.Label(self, text="First Name", font=LABELFONT).place(anchor=tk.CENTER, relx=0.3, rely=0.3)
        tk.Label(self, text="Last Name", font=LABELFONT).place(anchor=tk.CENTER, relx=0.3, rely=0.4)
        tk.Label(self, text="Birthday", font=LABELFONT).place(anchor=tk.CENTER, relx=0.3, rely=0.5)
        tk.Label(self, text="Likes", font=LABELFONT).place(anchor=tk.CENTER, relx=0.3, rely=0.6)
        tk.Label(self, text="Dislikes", font=LABELFONT).place(anchor=tk.CENTER, relx=0.3, rely=0.7)
        tk.Label(self, text="Additional", font=LABELFONT).place(anchor=tk.CENTER, relx=0.3, rely=0.8)

        e0 = tk.Entry(self)
        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        e3 = tk.Entry(self)
        e4 = tk.Entry(self)
        e5 = tk.Entry(self)
        e6 = tk.Entry(self)

        submit_button = ttk.Button(self, text="Update", command=submit_update)
        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))

        label.place(anchor=tk.CENTER, relx=0.5, rely=0.1)
        e0.place(anchor=tk.CENTER, relx=0.7, rely=0.2)
        search_button.place(anchor=tk.CENTER, relx=0.85, rely=0.2)
        e1.place(anchor=tk.CENTER, relx=0.7, rely=0.3)
        e2.place(anchor=tk.CENTER, relx=0.7, rely=0.4)
        e3.place(anchor=tk.CENTER, relx=0.7, rely=0.5)
        e4.place(anchor=tk.CENTER, relx=0.7, rely=0.6)
        e5.place(anchor=tk.CENTER, relx=0.7, rely=0.7)
        e6.place(anchor=tk.CENTER, relx=0.7, rely=0.8)
        submit_button.place(anchor=tk.CENTER, relx=0.3, rely=0.9)
        back_button.place(anchor=tk.CENTER, relx=0.7, rely=0.9)


# delete page
class DeletePage(tk.Frame):
    # init function for the starting page
    def __init__(self, parent, controller):
        # initialize the class as a tkinter Frame
        tk.Frame.__init__(self, parent, height=SCREEN_HEIGHT, width=SCREEN_WIDTH)

        # functions
        def submit_search():
            cursor.execute("SELECT * FROM Friends WHERE id=%s", (e0.get(),))
            text = ""
            for friend in cursor:
                text += "ID: " + str(friend[0]) + ", Name: " + friend[1] + " " + friend[2] + ", " + "Birthday: " + \
                        friend[3] + ", " + "Likes: " + friend[4] + ", " + "Dislikes: " + friend[5] + \
                        " Additional: " + friend[6] + "\n\n"
            if len(text) == 0:
                text += "There are no friends in the database with that name"
            friends_label_text.set(text)

        def delete_submit():
            cursor.execute("DELETE FROM Friends WHERE id=%s", (e0.get(),))
            db.commit()

        # starting page design
        label = ttk.Label(self, text="Delete a friend", font=FONT)
        tk.Label(self, text="ID of friend to update", font=LABELFONT).place(anchor=tk.CENTER, relx=0.3, rely=0.3)
        ttk.Button(self, text="Search for ID", command=submit_search).place(anchor=tk.CENTER, relx=0.5, rely=0.4)
        friends_label_text = tk.StringVar(value="")
        tk.Label(self, textvariable=friends_label_text).place(anchor=tk.CENTER, relx=0.5, rely=0.5)

        delete_button = ttk.Button(self, text="Delete", command=delete_submit)
        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))

        e0 = tk.Entry(self)

        label.place(anchor=tk.CENTER, relx=0.5, rely=0.1)
        e0.place(anchor=tk.CENTER, relx=0.7, rely=0.3)
        delete_button.place(anchor=tk.CENTER, relx=0.3, rely=0.9)
        back_button.place(anchor=tk.CENTER, relx=0.7, rely=0.9)


screen = FriendsManager()
screen.mainloop()
