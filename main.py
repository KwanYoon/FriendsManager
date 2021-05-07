import mysql.connector
import os
import tkinter as tk

# sql connection after initialization
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.environ['PASSWORD'],
    database="FriendsManager"
)
cursor = db.cursor()

# GUI / Main functionalities
SCREEN_HEIGHT, SCREEN_WIDTH = 600, 600

screen = tk.Tk()
screen.title("Friends Manager")

tk.Canvas(screen, height=SCREEN_HEIGHT, width=SCREEN_WIDTH).pack()

screen.mainloop()
