# Print given value is positive or not  
n=int(input("Enter the number:"))
if(n>0):
    print("Positive")
elif(n<0):
    print("Negative")
else:
    print("Zero")


# Given char(n) is upper case or lower case(without using built in function) 
ch=input("Enter a character:")
if ("A"<=ch<="Z"):
    print("UpperCase")
elif ("a"<=ch<="z"):
    print("LowerCase") 



# Pass or fail(have 6subject) eg:s1>35  
a=int(input("Enter subject marks:"))
b=int(input("Enter subject marks:"))
c=int(input("Enter subject marks:"))
d=int(input("Enter subject marks:"))
e=int(input("Enter subject marks:"))
f=int(input("Enter subject marks:"))
if (a>35 and b>35 and c>35 and d>35 and e>35 and f >35):
    print("Pass")
else:
    print("Fail")