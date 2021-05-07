import mysql.connector
import os

# creating database
db_setup = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.environ['PASSWORD']
)
setup_cursor = db_setup.cursor()

setup_cursor.execute("CREATE DATABASE FriendsManager")


# creating friend table
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.environ['PASSWORD'],
    database="FriendsManager"
)
cursor = db.cursor()

cursor.execute("CREATE TABLE Friends (first_name VARCHAR(15), last_name VARCHAR(15), birthday DATE, "
               "likes VARCHAR(50), dislikes VARCHAR(50), additional VARCHAR(100))")
