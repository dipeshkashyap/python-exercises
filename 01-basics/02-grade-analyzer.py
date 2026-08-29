# Grade Analyzer

num = int(input("Enter Your Marks: "))

if num < 0:
    print("Invalid marks")
elif num <= 39:
    print("Marks: ", num)
    print("Grade: F")
elif num <= 59:
    print("Marks: ", num)
    print("Grade: E")
elif num <= 69:
    print("Marks: ", num)
    print("Grade: D")
elif num <= 79:
    print("Marks: ", num)
    print("Grade: C")
elif num <= 89:
    print("Marks: ", num)
    print("Grade: B")
elif num <= 100:
    print("Marks: ", num)
    print("Grade: A")
else:
    print("Invalid marks")