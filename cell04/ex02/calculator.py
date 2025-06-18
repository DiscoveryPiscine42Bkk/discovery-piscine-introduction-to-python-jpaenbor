num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (cannot divide by zero)"
    
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
    print(f"{num1} / {num2} = {div}")