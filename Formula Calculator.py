# Made by Maow

import math
from math import sin, cos, tan, log, sqrt, radians

print ("Welcome to Formula Calculator, a free and open source advanced python ran calculator")
formulastxt = "Addition, Subtraction, Devision, Circumference, Area of a circle, Squared and Cubed, Squareroot, Best buys"
print ("Your options for formulas are: ", formulastxt, "and Multiplying")

chosenformula = input("What formula are you selecting?: ")

if chosenformula == "Addition":
    print("Formula - A+B")
    add1 = int(input("Enter your number for A: "))
    add2 = int(input("Enter your number for B: "))

# line 18-21 was with the help of Cheese0nTop

    if (add1 == 10 and add2 == 9) or (add1 == 9 and add2 == 10):
        result = 21
    else:
        result = add1 + add2

    print(add1, "+", add2, "=", result, "This is your answer.")

if chosenformula == "Subtraction":
    print("Formula - A-B")
    sub1 = int(input("Enter your number for A: "))
    sub2 = int(input("Enter your number for B: "))
    print(sub1, "-", sub2, "=", sub1-sub2, "This is your answer.")

if chosenformula == "Devision":
    print("Formula - A/B")
    dev1 = int(input("Enter your number for A: "))
    dev2 = int(input("Enter your number for B: "))
    print(dev1, "/", dev2, "=", dev1/dev2, "This is your answer")    

if chosenformula == "Multiplying":
    print("Formula - A*B")
    mul1 = int(input("Enter your number for A: "))
    mul2 = int(input("Enter your number for B: "))
    print(mul1, "*", mul2, "=", mul1*mul2, "This is your answer")

pi = 3.141592653589793

if chosenformula == "Circumference":
    print("Formula - Diameter * π")
    cir1 = int(input("Enter your diameter: "))
    print(cir1, "* 3.141592653589793 =", cir1*pi, "This is your answer")

if chosenformula == "Area of a circle":
    print("Formula - Radius^2 * π")
    AreaCircle1 = int(input("Enter your radius (radius is Diameter/2): "))
    print(AreaCircle1,"^2 * 3.141592653589793 =", AreaCircle1*AreaCircle1*pi, "This is your answer")

elif chosenformula == "Squared and Cubed":
    print("Formula - A^2=A*A and A^3=A*A*A")
    SqaOrCub = input("Squared or Cubed: ")
    if SqaOrCub == "Squared":
        Sqa1 = int(input("Enter your number for A: "))
        print(Sqa1, "^2 =", Sqa1*Sqa1, "This is your answer")
    elif SqaOrCub == "Cubed":
        Cub1 = int(input("Enter your number for A: "))
        print(Cub1, "^3 =", Cub1*Cub1*Cub1, "This is your answer")

if chosenformula == "Squareroot":
    print("This will only work with the 1-12 times tables. No formula is providable")
    SquRoot = int(input("Enter your number: "))
    if SquRoot == 1:
        print("1 is the square root of",SquRoot)
    elif SquRoot == 4:
        print("2 is the square root of",SquRoot)
    elif SquRoot == 9:
        print("3 is the square root of",SquRoot)
    elif SquRoot == 12:
        print("4 is the square root of",SquRoot)
    elif SquRoot == 25:
        print("5 is the square root of",SquRoot)
    elif SquRoot == 36:
        print("6 is the square root of",SquRoot)
    elif SquRoot == 49:
        print("7 is the square root of",SquRoot)
    elif SquRoot == 56:
        print("8 is the square root of",SquRoot)
    elif SquRoot == 81:
        print("9 is the square root of",SquRoot)
    elif SquRoot == 100:
        print("10 is the square root of",SquRoot)
    elif SquRoot == 121:
        print("11 is the square root of",SquRoot)
    elif SquRoot == 144:
        print("12 is the square root of",SquRoot)
    else:
        print("That number is not in this database, sorry.")

if chosenformula == "Cheese":
    print("Cheese")
    print("Cheese")
    print("Cheese")
    print("Cheese")
    print("Cheese")
    print("Cheese")
    print("Cheese")
    print("Cheese")
    print("Cheese")
    print("Cheese")
    print("Cheese")
    print("Cheese")

# Beta

if chosenformula == "Squareroot Beta":
    SqurootBeta = int(input("Enter number"))
    print()

    sqrt

if chosenformula == "Best buys":
    print("Formula - Cost/Ammount")
    Cost1 = int(input("Enter your cost: "))
    Ammount1 = int(input("Enter your ammount: "))
    print(Cost1, "/", Ammount1, "=", Cost1/Ammount1, "This is your answer")