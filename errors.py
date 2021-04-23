print("This program will divide 2 numbers")

stop_word = "stop"
while True:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    try:
        num1 = float(num1)
        num2 = float(num2)
        print("Result: " + str(num1 / num2))
    except ValueError as e:
        print("Error:" + str(e))
    except ZeroDivisionError as e:
        print("Error: division by zero")