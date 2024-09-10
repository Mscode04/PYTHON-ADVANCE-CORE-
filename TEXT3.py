def writef():
    L=["apple is fruit\n","hello python\n","hello good morninig"]
    f1.writelines(L)
def copyA():
    f1.seek(0)
    lines=f1.readlines()
    for i in lines:
        if "a" not in i:
            f2.write(i)
    f2.seek(0)
    l1=f2.read()
    for i in l1:
        print(i,end="")
with open("file1txt","w+") as f1,open("filectxt","w+")  as f2:
    writef()
    copyA()
