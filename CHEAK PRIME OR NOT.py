n=int(input("enter the number want to cheak:  "))
chek=0
if n==1:
    print(" not a prine")
elif n>1:
     for i in range(2,n\):
            if n % i ==0:
                chek=1
                break
     if chek==1:
           print(n," is  not a prime")
     else:
         print(n,"is a prime")
else:
    print("is not a prime")
