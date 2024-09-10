import csv
def ADD():
    CF=open("record.csv","w",newline="")
    obj=csv.writer(CF)
    while True:        
        Eid=int(input("enter employee id:  "))
        Ename=input("enter employee name:  ")
        Esalary=float(input("enter salary:  "))
        data=[Eid,Ename,Esalary]
        obj.writerow(data)
        Ans=input(" Do you whish to continue (y/n):  ")
        if Ans in "nN":
            break
    CF.close()
def COUNT():
    CF=open("record.csv","r")
    Rec=csv.reader(CF)
    count=0
    for x in Rec:
        count+=1
    print(" numer of records in csv file is: ",count)
    CF.close()
ADD()
COUNT()


        
