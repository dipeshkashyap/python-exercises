# Number Analyzer

num = int(input("Enter a Number: "))

if num > 0:
    print("Type: Positive")
elif num < 0:
    print("Type: Negative")
else:
    print("Type: Zero")

if num % 2 == 0:
    print("Parity: Even")
else:
    print("Parity: Odd")

print("Square:", num ** 2)