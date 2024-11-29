
from calculation import *

a = int(input("Enter first value "))
b = int(input("Enter second value "))
operand = input("Enter an operand to perfom calculation e.g. (+,-,*,/) ")

match operand:
    case "+":
        print(add(a,b))
    case "-":
        print(subtract(a,b))

    case "*":
        print(multiply(a,b))

    case "/":
        print(divide(a,b))

    case "_":
        print("Invalid operand")

