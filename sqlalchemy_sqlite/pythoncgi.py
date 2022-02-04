#!C:\Program Files\Python310\python

print("Content-Type:text/html")
print()

import cgi

print("<h1> Welcome to Python </h1>")
print("<hr/>")
print("<h1>Using input tag </h1>")
print("<body bgcolor='red' ")

form=cgi.FieldStorage()

id=form.getvalue("id")
name=form.getvalue("name")
lastname= form.getvalue("lastname")


import sqlite3

con = sqlite3.connect('sqlite:///college.db')
cur = con.cursor()

for row in cur.execute('SELECT * FROM students;'):
    print(row)


con.close()


