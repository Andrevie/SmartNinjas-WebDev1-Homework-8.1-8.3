x = int(input("Choose one number: "))

y = int(input("Choose some OTHER number: "))

calculation = input("What do you want these numbers to do? + or - or * or / ? You choose: ")

if calculation == "+":
    print(x + y)

if calculation == "-":
    print(x - y)

if calculation == "*":
    print(x * y)

if calculation == "/":
    print(x / y)

else:
    print("Error. You need to put in numbers or anything that allows me to do mathematical stuff!")

