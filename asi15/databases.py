#Q1

import sqlite3
try:
    c=sqlite3.connect('Students.db')
    print(con)
except sqlite3.DatabaseError as e:
    if c:
        print('Problem Occured') 
finally:
    c.close()
    print('DATABASE CREATED')

#Q2
info=[]
for n in range(1,11):

    info.append((input('Name:'),int(input('Marks:'))))

#Q3
import sqlite3
try:
    c=sqlite3.connect('Students.db')
    cursor=c.cursor()
    query='create table Students(name varchar(15),marks number(3) check (marks>=0 and marks<=100))'
    cursor.execute(query)
    print('TABLE CREATED')
    c.commit()
except sqlite3.DatabaseError as e:
    if c:
        c.rollback()
        print('Problem Occured')
finally:
    if cursor:
        cursor.close()
    if c:
        c.close()
    print('DONE!')
                
import sqlite3
try:
    c=sqlite3.connect('Students.db')
    cursor=c.cursor()
    query='insert into Students (name,marks) values (?,?)'
    cursor.executemany(query,info)
    c.commit()
    print('VALUES INSERTED')
    quer="select * from Students"
    cursor.execute(quer)
    data=cursor.fetchall()
    for row in data:
        print("NAME:{} , MARKS:{}" .format(row[0],row[1]))
    c.commit()
except sqlite3.DatabaseError as e:
    if c:
        c.rollback()
        print('Problem Occured')
finally:
    if cursor:
        cursor.close()
    if c:
        c.close()
    print('3rd DONE!')


#Q4    
import sqlite3
try:
    c=sqlite3.connect('Students.db')
    cursor=c.cursor()
    query="select * from Students where marks > 80"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        print("NAME:{} , MARKS:{}" .format(row[0],row[1]))
    c.commit()
except sqlite3.DatabaseError as e:
    if c:
        c.rollback()
        print("Problem occured:",e)
finally:
    if cursor:
        cursor.close()
    if c:
        c.close()
    print("ALL DONE!")



















