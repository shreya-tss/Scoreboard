import tkinter as tk
from prettytable import PrettyTable
import mysql.connector




root = tk.Tk()
root.geometry("1000x10000")
root.configure(background="blue")

#connect to mysql
cnx = mysql.connector.connect(user='root', password='Shreya', host='localhost', database='c4')
cursor = cnx.cursor()

#retrieve data
cursor.execute("SELECT DISTINCT * FROM Player ORDER BY scorepoints DESC;")
data = cursor.fetchall()

# create table
x = PrettyTable()
x.field_names = [i[0] for i in cursor.description]
for row in data:
    x.add_row(row)


#create label

label = tk.Label(root, text=x.get_string(), font=("Courier", 12),fg="black",bg="orange")
label.configure(width=800, height=800)
lb=tk.Label(root,text="LEADERBOARD",font=("Helvetica", 24),fg="black",bg="blue")
lb.pack()



label.pack()

root.mainloop()
