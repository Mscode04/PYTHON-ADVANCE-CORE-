num=int(input("enter a number to find its factor"))
print(1,end=' ')
factor=2
while factor <+num/2:
    if num % factor==0:
        print(factor,end= ' ')
    factor += 1 
print(num, end=' ')     
