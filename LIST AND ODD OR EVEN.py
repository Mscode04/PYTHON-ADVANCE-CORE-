x0=[]
x1=[]
x2=[]
i=0
element=int(input("number of elelment should you add:  "))
while i <element:
      x=int(input("element want to add:  "))
      x0.append(x)
      i=i+1
print("themain list:  ", x0)
for j in x0 :
    if j %2==0:
        x1.append(j)
    elif j==0:
        x3.append(j)
    else:
        x2.append(j)
print("The list of even numbers:  ",x1)        
print("The list of odd numbers:  ",x2)
print(" the count of the main list:   ", len(x0))



