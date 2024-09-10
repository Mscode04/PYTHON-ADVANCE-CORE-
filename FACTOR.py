n=int(input("enter the number to get factors:  "))
print(1)
if n>1:
    for i in range(2,int(n/2)):
        if n % i ==0:
            print(i)
print(n)
