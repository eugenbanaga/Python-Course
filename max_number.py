print("Description: This program will find the biggest value of 2 numbers")

x = input("Please enter first number: ")
y = input("Please enter second number: ")

x = float(x)
y = float(y)

if x > y:
    max_number = x
    info = "first number is greater than second"
elif y > x:
    max_number = y
    info = "second number is greater than first"
elif x == y:
    max_number = None
    info = "Numbers are even"
else:
    info = "Unexpected behavior"

print(info)
if max_number:
    print("Greatest number value:" + str(max_number))
