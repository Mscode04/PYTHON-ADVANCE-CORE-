import pickle
def writeEmp():    
        Eno=int(input("enter employee No:  "))
        Ename=input("enter employee name:  ")
        Esalary=float(input("enter salary:  "))
        Emp=[Eno,Ename,Esalary]
        pickle.dump(Emp,F)
def Display():
    F.seek(0)
    while True:
        try:
            Rec=pickle.load(F)
            print(Rec)
        except EOFError:
            pass
with open('Employww.dat','wb+') as F:
    n=int(input("enter number of employees: "))
    for i in range(0,n):
        writeEmp()
    Display()
             
