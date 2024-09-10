import pickle
def writestud():
    Sno=int(input("Enter roll no "))
    Sname=input("Enter name ")
    M=float(input("enter the marks "))
    S=[Sno,Sname,M]
    pickle.dump(S,F)
def updateb(rno):
    F.seek(0)
    flag=0
    while True:
        try:
            Rec=pickle.load(F)
            if Rec[0]==rno:
                print(Rec[1],Rec[2])
                Rec[2]=float(input('enter new marks '))
                flag=1
                break
        except EOFError:
                pass
    if flag==1:
         F.seek(0)
         pickle.dump(Rec,F)
         print("successfully updated!!!")
with open('stude.dat','wb+')as F:
    std=int(input("enter the number of students "))
    for i in range (std):
        writestud()
    rno=int(input('Enter rollno where mark is to be updated '))    
    updateb(rno)            
