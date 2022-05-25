def add(a,b):
    answer = a+b
    return answer

def subtract(x,y):
    answer = x - y
    return answer

def multiply(a,b):
    answer = a * b
    return answer

def divide(x,y):
    answer = x / y
    return answer

def modulus(a,b):
    answer = a % b
    return answer

def exponent(x,y):
    answer = x**y
    return answer

def integer_division(x,y):
    answer = x // y
    return answer

def square(b):
    answer = b * b
    return answer

def cube(c):
    answer = c * c * c
    return answer

# x = int(input("Enter number"))
def factorial(a):
    fact = 1
    for i in range(1,a +1):
        fact *= i
    return fact