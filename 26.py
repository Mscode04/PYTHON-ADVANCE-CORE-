num=int(input("enter a number "))
fact=1
if num<0:
    print("don't exist for negative numbers")
elif num==0:
    print("thae factorial of 0 is 1")
else:
    for x in range(1,num+1):
        fact=fact*x
    print("factorial of ",num,"is",fact)    
