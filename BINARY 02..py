import pickle
def writestud(i):
    Sname=input("Enter name")
    S=[i,Sname]
    pickle.dump(S,F)
def Display():
    F.seek(0)
    flag=0
    Rno=int(input("Enter roll no to be searched for"))
    while True:
        try:
            Rec=pickle.load(F)
            if Rec[0]==Rno:
                print(Rec[1])
                flag=1
                break
        except EOFError:
                pass
    if flag==0:
            print("serch RollNo is not found")
with open("studentfile.dat","wb+") as F:
    std=int(input("enter the number of students"))
    for i in range (1,std+1):
        writestud(i)
    Display()
    
    
