import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully";

conn.execute('CREATE TABLE students (name TEXT, email TEXT, phone TEXT, college TEXT, dep TEXT,facad TEXT,hod TEXT,dean TEXT,father TEXT,fathermob TEXT,mother TEXT,mothermob TEXT)')
print "Table created successfully";
conn.close()