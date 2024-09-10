def writef():
    L=["hello python\n","python is good"]
    f.writelines(L)
def displayf():
    f.seek(0)
    x=f.readlines()
    for i in x:
        for j in i.split():
            print(j+"#",end=" ")
        print()
with open("lab1.txt","w+") as f:
    writef()
    displayf()                 


         
