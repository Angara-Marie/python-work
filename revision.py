amount = 0
units = int(input("Enter number of units"))
if units <= 100:
    print(f"{amount} is 0")
elif units >100 and units <= 200:
    amount = (units - 100)*5
    print(amount)
elif units > 200:
    amount = 500 + (units -200)*10
    print(amount)

age = int(input("Enter your age"))
if age >= 18:
    print("Eligible to vote")
else :
    print("Not eligible to vote")

number = int(input("Enter number"))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

num = int(input("Enter number"))
if num % 5 == 0:
    print("Hello")
else:
    print("Bye")

