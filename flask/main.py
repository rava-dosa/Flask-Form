import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully";

conn.execute('CREATE TABLE students (name TEXT, email TEXT, phone INTEGER,year TEXT, college TEXT,cg TEXT, dep TEXT,facad TEXT,hod TEXT,dean TEXT,father TEXT,fathermob INTEGER,mother TEXT,mothermob INTEGER)')
print "Table created successfully";
conn.close()