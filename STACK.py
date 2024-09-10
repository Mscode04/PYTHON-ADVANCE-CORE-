Employee=[]
c="y"
while(c=="y"):
    print("1.PUSH")
    print("2.POP")
    print("3.Display")
    choice=int(input("enter your choice"))
    if (choice==1):
        eid=input("Enter employee id")
        ename=input("Enter employee name: ")
        emp=[eid,ename]
        Employee.append(emp)
    elif(choice==2):
        if(Employee==[]):
            print("stack empty")
        else:
            eid,ename=Employee.pop()
            print("Deleted element is: ",eid,ename)
    elif(choice==3):
        i=len(Employee)
        while i>0:
            print(Employee[i-1])
            i=i-1
    else:
        print("wrong input")
    c=input("Do you want to continue or not?")
    
                     
                     
                     
