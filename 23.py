num=int(input("enter the number to be cheacked: "))
flag=0
if num>1:
        for i in range (2,int(num/2)):
            if num%i==0:
              flag=1
              break
        if flag==1:
          print(num,"not prime")
        else:
            print(num,"is a prime")
else:
    print("number<=1,execute again")
         
              
    
