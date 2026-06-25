#  1.sum of list 
l=[1,2,3,4,5,6,2,3,4,8]
count=0
for i in range(len(l)):
    count=count+l[i]
print(count)

        #OR

l=[1,2,3,4,5,6,2,3,4,8]
print(sum(l))    




#  product of the list 
l=[1,2,3,4,5,6]
count=1
for i in range(len(l)):
    count=count*l[i]
print(count)

        #OR

l=[1,2,3,4,5,6]
import math
print(math.prod(l))
 



#   max,min,length of list 
l = [12, 45, 7, 89, 23, 56, 91, 34]
max1=l[0]
min1=l[0]
count=0
for i in range(1,len(l)):
    if (max1<l[i]):
        max1=l[i]
    elif (min1>=l[i]):
        min1=l[i]
for i in l:
    count=count+1
print(max1,min1,count)

        #OR
l = [12, 45, 7, 89, 23, 56, 91, 34]
print(max(l),min(l),len(l),end="   ")

