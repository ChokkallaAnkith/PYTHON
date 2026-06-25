#Sum of Digits  1234 → 10 
n=1234
s=str(n)
count=0
for i in range(len(s)):
    count=count+int(s[i])
print(count)


#Reverse a Number 1234 → 4321    
n=1234
result=0
while n>0:
    temp=n%10
    result=result*10+temp
    n//=10
print(result)


#Count Digits in a Number  12345 → 5 
n=12345
s=str(n)
count=0
for i in range(len(s)):
    count=count+1
print(count)

Check Even or Odd  17 → Odd 
n=17
if(n%2==0):
    print("Even")
else:
    print("Odd")


# Check Prime Number   13 → Prime 
n=13
count=0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
if(count==2):
    print("Prime")
else:
    print("Not Prime")


#Find Factorial of a Number     5 → 120   
n=5
count=1
for i in range(1,n+1):
    count=count*i
print(count)


#Find Factors of a Number 12 → 1, 2, 3, 4, 6, 12 
n=12
for i in range(1,n+1):
    if (n%i==0):
        print(i,end=" ")


#| Check Palindrome Number  121 → Palindrome
n=121
m=n
result=0
while n>0:
    temp=n%10
    result=result*10+temp
    n//=10
c=result
if(m==c):
    print("Palindrome")
else:
    print("Not Palinmdrome") 


#Check Armstrong Number  153 → Armstrong
n=153
m=n
s=str(n)
l=len(s)
count=0
for i in range(l):
    count=int(s[i])**l+count
if(count==n):
    print("Armstrong")
else:
    print("Not Armstrong")


#Find GCD (HCF) of Two Numbers  12, 18 → 6
a=12
b=18
gcd=0
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
print(gcd)