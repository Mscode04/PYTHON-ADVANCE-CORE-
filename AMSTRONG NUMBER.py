n=int(input("number: "))
x=0
y=n
while y >0:
    d=y%10
    x=x+d**3
    y=y//10
if n==x:
    print("Amstrong number")
else:
    print(" NOT Amstrong numbe")
    
