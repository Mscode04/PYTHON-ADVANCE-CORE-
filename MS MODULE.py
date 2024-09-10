def fav(x):
    if x=="aban":
        print("ali khan")
    elif x=="mazin":
        print("shehzad")
    elif x=="shehzad":
        print("ariyen")        
    elif x=="ali khan":
        print("aban")
    elif x=="shaad":
        print("gouthem")
    elif x=="shifin":
        print("not defined")
    elif x=="sanju":
        print("anjana")
    elif x=="fasil":
        print("chinnu")
    elif x=="shaheen":
        print("___")
    elif x=="tuttu":
        print("me")          
    else:
         print("add your data in to module")
         
def add():
      x=float(input("( ADDITION)enter 1st numer you want"))
      y=float(input("( ADDITION) enter 2st numer you want"))    
      A=x+y
      return A
def sub():
      x=float(input("(SUBTRACT)enter 1st numer you want"))
      y=float(input("(SUBTRACT)enter 2st numer you want"))    
      a=abs(x-y)
      return a
def mul():
      x=float(input("(MULTIPLICATION)enter 1st numer you want"))
      y=float(input("(MULTIPLICATION)enter 2st numer you want"))    
      b=x*y
      return b
def div():
      x=float(input("(DIVISION)enter 1st numer you want"))
      y=float(input("(DIVISION)enter 2st numer you want"))       
      if y==0:
          print("not defined. enter valid number")
      else:
          return x/y
def power():
      x=float(input("(POWER) enter the numer"))
      y=float(input("(POWER) enter the power") )                     
      g=x**y
      return g
def sqr():
      x=float(input("(squre) enter the numer"))
      f=x**2
      return f
def letter1():
      h=input("enter date ")
      y=input("enter you name:  ")
      x=input("enter friend's name:  ")
      z=input("enter the body of letter:  ")
      print("       ")
      print(h)
      print("       ")
      print("Dearest ",x)
      print("       ")
      print("I hope you have been having a wonderful. ",z," .Hoping to hear from you soon.")
      print("       ")
      print("       ") 
      print("     Yours sincerely,")
      print("       ") 
      print("     Have a nice day ")
      print("       ") 
      print("     Lovingly ",y)
      print("     Bye")
def fv(x):
    pack={"shaheen":"naphthaline","shehzad":"jhon"}
    if x in pack:
        print(pack[x])
    else:
        print(" you are not register in the pack")
        c=input("enter your favorate name:   ")
        pack[x]=c
        print(" your favorate person or name : ",pack[x])
        
        
      
              
              








    
     


 

         





              

