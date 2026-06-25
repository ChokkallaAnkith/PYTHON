#Write a program to find the area of a rectangle.
l=int(input("Enter the value:"))
b=int(input("Enter the value:"))
area=l*b
print("Area is",area)

#Write a program to find the area of a square.
a=int(input("Enter the value:"))
area=a*a
print("Area is",area)

#Write a program to find the area of a triangle.
h=int(input("Enter the value:"))
b=int(input("Enter the value:"))
area=0.5*h*b
print("Area is",area)

#Write a program to find the area of a circle.
r=int(input("Enter the value:"))
area=3.14*r*r
print("Area is",area)

#Write a program to find the area of a parallelogram.
b=int(input("Enter the value:"))
h=int(input("Enter the value:"))
area=b*h
print("Area is",area)

#Write a program to find the area of a rhombus.
d1=int(input("Enter the value:"))
d2=int(input("Enter the value:"))
area=0.5*d1*d2
print("Area is",area)

#Write a program to find the area of a trapezium.
a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
h=int(input("Enter the value"))
area=0.5*h*(a+b)
print("Aera is",area)

#Write a program to find the area of an equilateral triangle.
a=int(input("Enter the value:"))
area=0.433*(a*a)
print("Aera is ",area)

#Write a program to find the area of a sector of a circle.
x=int(input("Enetr the value:"))
r=int(input("Enetr the value:"))
print("Area is:",(x/360)*3.14*r*r)

#Write a program to find the area of a semicircle.
r=int(input())
print("Area is:",0.5*3.14*r*r)


#PERIMETER PROBLEMS

#RECTANGLE
l=int(input("Enter the value:"))
b=int(input("Enter the value:"))
p=2*(l+b)
print("Perimeter is",p)

#SQUARE
a=int(input("Enter the value:"))
p=4*a
print("Perimeter is",p)

#CIRCLE
r=int(input("Enter the value:"))
p=3.14*r*2
print("Perimeter is",p)

#TRIANGLE
l=int(input("Enter the value:"))
h=int(input("Enter the value:"))
b=int(input("Enter the value:"))
p=l+b+h
print("Perimeter is",p)

#PARALLELOGRAM
b=int(input("Enter the value:"))
a=int(input("Enter the value:"))
p=2*(a+b)
print("Perimeter is",p)

#RHOMBUS
a=int(input("Enter the value:"))
p=4*a
print("Perimeter is",p)

#REGULAR PENTAGON
a=int(input("Enter the value:"))
p=5*a
print("Perimeter is",p)

#REGULAR HEXAGON
a=int(input("Enter the value:"))
p=6*a
print("Perimeter is",p)

#TRAPEZIUM
a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
c=int(input("Enter the value:"))
d=int(input("Enter the value:"))
print("Perimeter is:",a+b+c+d)

#EQULIATERAL TRIANGLE
a=int(input("Enter the value:"))
p=3*a
print("Perimeter is",p)


#CUBES PROBLEMS
#VOLUME 
a=int(input("Enter the value:"))
v=a*a*a
print("Volume is:",v)

#Total Surface area
a=int(input("Enter the value:"))
ta=6*a*a
print("Total Surface area is:",ta)

#Lateral Surface area
a=int(input("Enter the value:"))
la=4*a*a
print("Lateral Surface area is:",ta)

#Cube of number
a=int(input("Enter the value:"))
v=a*a*a
print("cube of number  is:",v)

#Sum of cubes
a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
soc=(a+b)*((a*a)-(a*b)+(b*b))
print(soc)

#Difference of cube
a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
soc=(a-b)*((a*a)+(a*b)+(b*b))
print(soc)

#Sum of cubes from 1 to n
a=int(input("Enter the value:"))
print("Sum of cubes",(((a+1)*a)/2)*2)

#Cube root
a = int(input("Enter a number: "))
print("Cube root is", a ** (1/3))


