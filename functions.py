# def hello(name,age):
#     year = 2022 - age
#     print("Welcome to AkiraChix")
#     return
#     print(f"Hello {name}, you were born in {year}")


def hello(name,age):
    year = 2022 - age
    return f"Hello {name}, you were born in {year}"


def add(a,b):
    answer = a+b
    return answer

def my_country(country = "Uganda", student = "Susan"):
    return f"Hello {student} you are from {country}" 

# def greet_multiple(*names):
#     # print(names)       
#     for name in names:
#         print(f"Hello {name}")


# Write a function that accepts any number of integers and returns the sum of all of them 
def add(*numbers):
    sum = 0
    for num in numbers:
        sum+=num
    return sum    

def multiply(*numbers):
    times = 1
    for num in numbers:
        times*=num
    return times    

# def greet_multiple(**kwargs):
#     print(kwargs)    
#     print(kwargs.keys())
#     print(kwargs.values())


def greet_multiple(**kwargs):
    keys = kwargs.keys()
    if 'country' in keys:
        print( f"Hello {kwargs['name']} you  are from {kwargs['country']}")
    elif "age" in keys:
        year = 2022 - kwargs["age"]    
        print(f"Hello {kwargs['name']} you are born in {year} ")
    elif not kwargs:
        print("Hello, you are anonymous")

def sum_and_greet(*args, **kwargs):
    sum = 0
    for num in args:
        sum+=num
    keys = kwargs.keys()
    if 'name' in keys:
        print(f"Hello {kwargs['name']}, the answer is {sum}")  
    elif 'country' in keys:
        print(f"{kwargs['country']} the answer is {sum}")
        # print(f"Hello{kwargs['name']} from {kwargs['country']} the answer is {sum} ")
    elif not kwargs:
        print(f"Hello anonymus the answer is {sum}")