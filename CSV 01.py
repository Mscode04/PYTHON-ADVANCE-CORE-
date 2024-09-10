import csv 
def writercsv():
    cobj=csv.writer(CF)
    while True:
        uid=input("Enter the user id:  ")
        password=input("Ener passward: ")
        data=[uid,password]
        cobj.writerow(data)
        ans=input(" Do you whish to continue (y/n):  ")
        if ans in "nN":
            break
def display():
    CF.seek(0)
    uid=input("Enter user id to be search for:  ")
    rec=csv.reader(CF)
    for i in rec:
        if i[0]==uid:
            print(i[1])
            break
with open("csvlab1.csv","w+",newline="") as CF:
    writercsv()
    display()
    
    
