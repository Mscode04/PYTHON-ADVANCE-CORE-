#####BANK MANAGMENT SYSYTEM#####
import mysql.connector as x
db=x.connect (host="localhost",user="root", passwd="admin")
c=db.cursor()
c.execute("create database if not exists rrr")
c.execute("use rrr")
c.execute("create table if not exists BANKMASTER(Acno int primary key,Name varchar(30),City varchar(20),Mobileno int,Balance int)")
c.execute("create table if not exists BANKTRANS(Acno varchar (6),amount int,Dot date,Ttype varchar(20),foreign key (Acno) references BANKMASTER(Acno))")
c.execute("create table if not exists EMPLOYEE_DATA(EmployeeID varchar(20) primary key, EmployeeName varchar(30), Age varchar(20), EmployeeSalary varchar(20))")
c.execute("create table if not exists EMPLOYEE_ATTENDANCE(EmployeeID int primary key , Name varchar(30), Date date, Status varchar(6))")
db.commit()
def menu():
   c=input("Do you want to open (Y/N)")
   while (c=="Y" or "y"):
         print("1=CREATE ACCOUNT")
         print("2=DEPOSIT MONEY")
         print("3=WITHDARW MONEY")
         print("4=DISPLAY ACCOUNT")
         print("5=ADD NEW EMPLOYEE")
         print("6=EMPLOYEE ATTENDANCE")
         print("7=EXIT")
         choice=int(input("ENTER YOUR CHOICE:  "))
         if choice ==1:
            CREATE_ACCOUNT()
         elif choice ==2:
             DEPOSIT_MONEY()
         elif choice ==3:
             WITHDRAW()
         elif choice ==4:
             DISPLAY_ALL_ACCOUNT_DETAILS()
         elif choice ==5:
             ADD_NEW_EMPLOYEE() 
         elif choice ==6:
            EMPLOYEE_ATTENDENCE()               
         elif choice ==7:
              break
   else:
         print("WRONG INPUT")
def  CREATE_ACCOUNT():
      print('WELCOME TO BANK05')
      print("ALL INFORMATION PROMPTED ARE MANDATORY TO BE FILLED")
      Acno=str(input("ENTER YOUR ACCOUNT NUMBER:"))
      Name=input("ENTER AC NAME:")
      City=str(input("ENTER YOUR CITY NAME:"))
      Mn=int(input("ENTER YOUR MOBILE NUMBER:"))
      Balance=0
      c.execute("insert into BANKMASTER values('"+str(Acno)+"','"+Name+"','"+City+"','"+str(Mn)+"','"+str(Balance)+"')")
      db.commit()
      db.close()
      print("ACCOUNT IS SUCCESSFULLY CREATED!!!")
def DEPOSIT_MONEY():
      Acno=str(input("ENTER ACCOUNT NUMBER:  "))
      Dp=int(input("ENTER AMOUNT TO BE DEPOSITED:  "))
      Dot=str(input("ENTER DATE OF DEPOSIT (YYYY-MM-DD) : "))
      Ttype="deposit"
      c.execute("insert into BANKTRANS values('"+Acno+"','"+str(Dp)+"','"+Dot+"','"+Ttype+"')")
      c.execute("update BANKMASTER set Balance=Balance+'"+str(Dp)+"' where Acno='"+Acno+"'")
      db.commit()
      db.close()
      print("MONEY HAS BEEN DEPOSITED SUCCESSFULLY!!!")
def WITHDRAW():
      Acno=str(input("ENTER ACCOUNT NUMBER:  "))
      Wd=int(input("ENTER AMOUNT TO BE WITHDRAWN:  "))
      Dot=str(input("ENTER DATE OF WITHDRAW (YYYY-MM-DD) :  "))
      Ttype="withdraw"
      c.execute("insert into BANKTRANS values('"+Acno+"','"+str(Wd)+"','"+Dot+"','"+Ttype+"')")
      c.execute("update BANKMASTER set balance=balance-'"+str(Wd)+"' where acno='"+Acno+"'")
      db.commit()
      db.close()
      print("MONEY HAS BEEN WITHDRAWN SUCCESSFULLY!!!")
def DISPLAY_ALL_ACCOUNT_DETAILS():
      Acno=str(input("ENTER ACCOUNT NUMBER:  "))
      c.execute("select * from BANKMASTER where acno='"+Acno+"'")
      result=c.fetchall()
      for x in result:
         print(x)           
def EMPLOYEE_ATTENDENCE():
      print("WELCOME TO EMPLOYEE ATTENDENCE WINDOW")   
      EmployeeID=str(input("ENTER EMPLOYEEID:   "))
      Name=input("ENTER NAME:   ")
      Date=str(input("ENTER DATE:   "))
      Status=str(input("ENTER STATUS A\P:   "))
      c.execute("insert into EMPLOYEEATTENDANCE values('"+EmployeeID+"','"+Name+"','"+Date+"','"+Status+"')")
      db.commit()
      db.close()
      print("ATTENDENCE IS ADDED")
def ADD_NEW_EMPLOYEE():
      print("WELCOME TO EMPLOYEE DETAILS WINDOW") 
      n=int(input("HOW MANY RECORDS SHOULD BE ADDED: "))
      i=0
      while i<n:             
           EmpID=str(input("ENTER EMPLOYEEID:   "))
           Name=input("ENTER YOUR NAME:   ")
           Age=str(input("ENTER YOUR AGE:   "))
           salary=str(input("ENTER SALARY:   "))
           c.execute("insert into EMPLOYEE1 values('"+str(EmpID)+"','"+Name+"','"+str(Age)+"','"+str(salary)+"')")
           db.commit()
           i=i+1

menu()

   
