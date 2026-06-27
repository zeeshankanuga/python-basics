num1=float(input("Enter first number1: "))
num2=float(input("Enter second number2: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    output = num1 + num2

if operator == '-':
    output = num1 - num2
    
if operator == '*':
    output = num1 * num2
    
if operator == '/':
    output = num1 / num2
    
print('your calculation is :', output)

if num1<3:
    print("num1 is less than 3")
elif num1==3:
    print("num1 is equal to 3")
else:
    print("num1 is greater than 3")