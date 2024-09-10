def rectangle():
    a=int(input("enter the length of rectangle"))
    b=int(input("enter the breadth of rectangle"))
    c=a*b
    print("area of rectangle is",c)
def cube():
    a=int(input("enter the length of cube"))
    c=6*a**2
    print("area of cube is",c)
def triangle():
    a=int(input("enter the base of triangle"))
    b=int(input("enter the height of the triangle"))
    c=0.5*a*b
    print("area of triangle is",c)
def circle():
    a=int(input("enter the radius of circle"))
    c=3.14*a**2
    print("area of circle is",c)
rectangle()
cube()
triangle()
circle()
