h=input("enter the file path:  ")
ck=input("enter what you want to cheak:   ")
x=open(h,"r")
k=""
for i in x:
    k=k+i
print(k)
if ck in k:
    print(ck, "in this file")
else:
    print("not in file")
x.close()

