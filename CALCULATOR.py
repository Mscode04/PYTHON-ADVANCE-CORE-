def add(x,y):
    A=x+y
    print("The addtion is",A)
def sub (x,y):
    S=abs(x-y)
    return S
def mul():
    a=int(input("enter mul 1 number"))
    b=int(input("enter mul 2 number"))
    C=a*b
    return C
def div():
    k=int(input("enter the first number"))
    l=int(input("enter the second number"))
    if l==0:
        print("not defined")
    print("div is",k/l)

#calling    
y=int(input("enter add1 number"))
j=int(input("enter add2 number"))
add(y,j)
subresult=sub(y,j)
print("sub is",subresult)
d=mul()
print("mul is ",d)
div()
             
 
