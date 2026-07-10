# 1. Function to Add Two Numbers

def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum =", add(num1, num2))


# 2. Function to Check Even or Odd

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"

n = int(input("Enter a number: "))
print(even_odd(n))


# 3. Function to Find Maximum of Three Numbers

def maximum(a, b, c):
    return max(a, b, c)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Maximum =", maximum(a, b, c))


# 4. Function to Calculate Factorial

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))


# 5. Function to Check Prime Number

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")


# 6. Function to Reverse a String

def reverse_string(text):
    return text[::-1]

text = input("Enter a string: ")
print("Reversed String =", reverse_string(text))


# 7. Function to Count Vowels

def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

word = input("Enter a word: ")
print("Vowel Count =", count_vowels(word))


# 8. Function to Find Sum of List Elements

def list_sum(numbers):
    return sum(numbers)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum =", list_sum(numbers))


# 9. Function to Check Palindrome

def palindrome(text):
    return text == text[::-1]

word = input("Enter a word: ")
if palindrome(word):
    print("Palindrome")
else:
    print("Not Palindrome")


# 10. Function to Calculate Square

def square(n):
    return n * n

num = int(input("Enter a number: "))
print("Square =", square(num))


# 11. Function to Check Armstrong Number

def armstrong(num):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == num

num = int(input("Enter a number: "))
if armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


# 12. Function to Check Strong Number

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def strong(num):
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10

    return total == num

num = int(input("Enter a number: "))
if strong(num):
    print("Strong Number")
else:
    print("Not a Strong Number")


# 13. Function to Check Perfect Number

def perfect(num):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total += i

    return total == num

num = int(input("Enter a number: "))
if perfect(num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")


# 14. Function to Check Leap Year

def leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

year = int(input("Enter a year: "))
if leap(year):
    print("Leap Year")
else:
    print("Not a Leap Year")


# 15. Function to Find Cube of a Number

def cube(n):
    return n ** 3

num = int(input("Enter a number: "))
print("Cube =", cube(num))