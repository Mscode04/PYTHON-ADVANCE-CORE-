#####BANK MANAGMENT SYSYTEM#####
import mysql.connector as x
db=x.connect (host="localhost",user="root", passwd="admin")
c=db.cursor()
c.execute("create database if not exists bank5")
c.execute("use bank5")
c.execute("create table if not exists BANKMASTER01(Acno int primary key,Name varchar(30),City varchar(20),Mobileno int,Balance int)")
c.execute("create table if not exists BANKTRANS01(Acno varchar (6),amount int,Dot date,Ttype varchar(20),foreign key (Acno) references BANKMASTER(Acno))")
c.execute("create table if not exists EMPLOYEE01(EmployeeID varchar(20) primary key, EmployeeName varchar(30), Age varchar(20), EmployeeSalary varchar(20))")
c.execute("create table if not exists EMPLOYEEATTENDANCE01(EmployeeID int primary key , Name varchar(30), Date date, Status varchar(6))")
db.commit()
def menu():
   c=input("Do you want to open (Y/N)")
   while (c=="Y" or "y"):
         print("1=Create Account")
         print("2=Deposit Money")
         print("3=Withdraw Money")
         print("4=Display Account")
         print("5=emlpyee atendencet")
         print("6=add new employee")
         print("7=Exit")
         choice=int(input("Enter your  choice:  "))
         if choice ==1:
            CREATE_ACCOUNT()
         elif choice ==2:
             DEPOSIT_MONEY()
         elif choice ==3:
             WITHDRAW()
         elif choice ==4:
             DISPLAY_ALL_ACCOUNT_DETAILS()
         elif choice ==5:
             EMPLOYEE_ATTENDENCE()
         elif choice ==6:
             ADD_NEW_EMPLOYEE()   
         elif choice ==7:
              break
   else:
         print("wrong input")
def  CREATE_ACCOUNT():
      print('WELCOME TO BANK05')
      print("ALL INFORMATION PROMPTED ARE MANDATORY TO BE FILLED")
      Acno=str(input("Enter  your account number:"))
      Name=input("Enter AC name:")
      City=str(input("Enter  your city name:"))
      Mn=int(input("Enteryour mobile number.:"))
      Balance=0
      c.execute("insert into BANKMASTER values('"+str(Acno)+"','"+Name+"','"+City+"','"+str(Mn)+"','"+str(Balance)+"')")
      db.commit()
      db.close()
      print("ACCOUNT IS SUCCESSFULLY CREATED!!!")
def DEPOSIT_MONEY():
      Acno=str(input("Enter account number:"))
      Dp=int(input("Enter amount to be deposited:"))
      Dot=str(input("Enter date of Transaction: YYYY-MM-DD "))
      Ttype="deposit"
      c.execute("insert into BANKTRANS values('"+Acno+"','"+str(Dp)+"','"+Dot+"','"+Ttype+"')")
      c.execute("update BANKMASTER set Balance=Balance+'"+str(Dp)+"' where Acno='"+Acno+"'")
      db.commit()
      db.close()
      print("MONEY HAS BEEN DEPOSITED SUCCESSFULLY!!!")
def WITHDRAW():
      Acno=str(input("Enter account number:"))
      Wd=int(input("Enter amount to be withdrawn:"))
      Dot=str(input("Enter date of transaction: YYYY-MM-DD "))
      Ttype="withdraw"
      c.execute("insert into BANKTRANS values('"+Acno+"','"+str(Wd)+"','"+Dot+"','"+Ttype+"')")
      c.execute("update BANKMASTER set balance=balance-'"+str(Wd)+"' where acno='"+Acno+"'")
      db.commit()
      db.close()
      print("MONEY HAS BEEN WITHDRAWN SUCCESSFULLY!!!")
def DISPLAY_ALL_ACCOUNT_DETAILS():
      Acno=str(input("Enter account number:"))
      c.execute("select * from BANKMASTER where acno='"+Acno+"'")
      result=c.fetchall()
      for x in result:
         print(x)           
def EMPLOYEE_ATTENDENCE():
      print("WELCOME TO EMPLOYEE ATTENDENCE WINDOW")   
      EmployeeID=str(input("Enter EmployeeID: "))
      Name=input("Enter Name: ")
      Date=str(input("Enter date: "))
      Status=str(input("Enter Status A\P: "))
      c.execute("insert into EMPLOYEEATTENDANCE values('"+EmployeeID+"','"+Name+"','"+Date+"','"+Status+"')")
      db.commit()
      db.close()
      print("ATTENDENCE IS ADDED")      
def ADD_NEW_EMPLOYEE():
      print("WELCOME TO EMPLOYEE DETAILS WINDOW") 
      n=int(input(" enter how many persons should be added: "))
      i=0
      while i<n:             
           EmpID=str(input("Enter EmployeeID: "))
           Name=input("Enter Name: ")
           Age=str(input("Enter age: "))
           salary=str(input("Enter salary: "))
           c.execute("insert into EMPLOYEE1 values('"+str(EmpID)+"','"+Name+"','"+str(Age)+"','"+str(salary)+"')")
           db.commit()
           i=i+1
      print("DETAILS IS ADDED")
menu()
