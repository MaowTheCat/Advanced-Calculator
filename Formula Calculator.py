# Made by Maow

import math

print ("Welcome to Formula Calculator, a free and open source advanced python ran calculator")
formulastxt = "Addition, Subtraction, Devision"
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