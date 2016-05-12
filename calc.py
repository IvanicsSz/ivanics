#!/usr/bin/env python
import sys,io
start = "\033[1m"
end = "\033[0;0m"

def calc(num1,num2,op):

    if (op=="+"):
        return num1+num2
    elif(op=="-"):
        return num1-num2
    elif (op=="*"):
        return num1*num2
    elif (op=="/"):
        return num1/num2
    else:
        return "Not supported operator only: +,-,*,/"

while True:
    number1=input("Enter a number (or a letter to "+start+"exit"+end+"):")
    try:
        nbr1=int(number1)
    except ValueError:
        exit()

    operator=input("Enter an operator:")

    number2=input("Enter another number:")
    nbr2=int(number2)

    print("Result:"+str(calc(nbr1,nbr2,operator)))
