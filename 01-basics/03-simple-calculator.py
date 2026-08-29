a = float(input("Enter First Number: "))

print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")

operator = input("Choose an Operator: ")
b = float(input("Enter Second Number: "))

if operator == "+":
    print("Result:", a + b)

elif operator == "-":
    print("Result:", a - b)

elif operator == "*":
    print("Result:", a * b)

elif operator == "/":
    if b == 0:
        print("Can't divide by Zero.")
    else:
        print("Result:", a / b)

else:
    print("Enter a valid Operator.")