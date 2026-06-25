#All operators
# Arithmetic Operators
a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# Comparison Operators
x = 20
y = 15

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Assignment Operators
p = 10
p += 5
print(p)

p -= 3
print(p)

p *= 2
print(p)

p /= 4
print(p)

p //= 2
print(p)

p %= 3
print(p)

p **= 2
print(p)

# Logical Operators
m = True
n = False

print(m and n)
print(m or n)
print(not m)

# Bitwise Operators
u = 12
v = 2

print(u & v)
print(u | v)
print(u ^ v)
print(~u)
print(u >> 2)
print(v << 2)

# Membership Operators
lst = [10, 20, 30, 40]

print(20 in lst)
print(50 not in lst)

# Identity Operators
a1 = [1, 2, 3]
a2 = a1
a3 = [1, 2, 3]

print(a1 is a2)
print(a1 is a3)
print(a1 is not a3)