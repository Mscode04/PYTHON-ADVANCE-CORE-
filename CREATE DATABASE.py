def createdb():
   import mysql.connector
   mydb=mysql.connector.connect(host="localhost",user="root",passwd="admin")
   cr=mydb.cursor()
   cr.execute("create database shahenxylem")
def createstudent():
   import mysql.connector 
   mydb=mysql.connector.connect(host="localhost",user="root",passwd="admin",database="shahenxylem")
   cr=mydb.cursor()
   cr.execute("create table student(rno integer primary key not null,sname varchar(20),mark integer,grade varchar(3),course varchar(20))")
#createdb()
createstudent()

