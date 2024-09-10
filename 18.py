result=0
no_1=float(input("enter  value 1: "))
no_2=float(input("enter  value 2: "))
op=input(" enter any one of the operator (+,-,*,/): ")
if op=="+":
    result=no_1+no_2
elif op =="-":
    if no_1>no_2:
        result=no_1-no_2
    else:
        result=no_2-no_1
elif op=="*":
    result=no_1*no_2
elif op=="/":
    if no_2==0:
        print("error!,divission by zero is not difined")
    result=no_1/no_2
else:
    print("worrg input, program terminated")
print("result is",result)     


        
