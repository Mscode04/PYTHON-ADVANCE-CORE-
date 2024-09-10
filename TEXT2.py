def writef():
    line=input("enter sentance:  ")
    f.write(line)
def countf():
    f.seek(0)
    x=f.read()
    v=0
    c=0
    u=0
    l=0
    for i in x:
        if i.isalpha():
            if i in "aeiouAEIOU":
                v+=1
            else:
                 c+=1
            if i.isupper():
                u+=1
            else:
                l+=1
    print("vowels  ",v)
    print("cosonants  ",c)
    print("upper case  ",u)
    print("lower case  ",l)
with open("lab2.txt","w+") as f:
    writef()
    countf()



   
