import math
import re

import functions

# PEMDAS
precedence={
    "^":4,
    "*":3,
    "/":3,
    "+":2,
    "-":2,
    "(":0,
    ")":0
}
def sqrt():
    userX=input("Enter number to square root\nWrite exit to go back: ")
    if userX == "exit":
        return ["exit", "exit"]
    return [userX,math.sqrt(float(userX))]

def calculate():
    # to do: add result as input, maybe !
    userX = input("Enter your calculation +,-,*,/,(),^\nWrite exit or leave empty to go back: ")

    if userX == "exit" or userX=="":
        return ["exit", "exit"]
    x=userX.replace(" ","")
    if x!=re.sub('[a-z]', '', x):
        raise TypeError

    expressionArray=[]

    lenOfX=len(x)

    digitLength=0

    # not pythonic, will fix later
    #divides expression into array with numbers and operators
    for i in range(lenOfX):
        if x[i].isdigit() or x[i]==".":
            digitLength+=1
        else:
            expressionArray.append(x[i-digitLength:i])
            expressionArray.append(x[i])
            digitLength=0
    expressionArray.append(x[lenOfX-digitLength:lenOfX])
    expressionArray = list(filter(None, expressionArray))
    oppStack=[]
    numQueue=[]

    #converts expression array into reverse polish notation (postfix)
    for i in expressionArray:
        if i.replace(".","").isdigit():
            numQueue.append(i)
        elif i=="(":
            oppStack.append(i)
        elif i==")":
            while oppStack:
                if oppStack[-1]!="(":
                    numQueue.append(oppStack.pop())
                else:
                    oppStack.pop()
                    break
        elif i=="^":
            oppStack.append(i)
        elif i=="*" or i=="/":
            while oppStack and precedence[oppStack[-1]]>=precedence[i]:
                numQueue.append(oppStack.pop())
            oppStack.append(i)
        elif i=="+" or i=="-":
            while oppStack and precedence[oppStack[-1]]>=precedence[i]:
                numQueue.append(oppStack.pop())
            oppStack.append(i)

    for i in range(len(oppStack)):
        numQueue.append(oppStack.pop())

    #goes through RPN array and operates
    result=[]
    for i in numQueue:
        if i.replace(".","").isdigit():
            result.append(i)
        else:
            result.append(functions.operation(result.pop(),result.pop(),i))
    if len(result)>1:
        raise NameError
    result=result[0]
    print ("Result:",result)
    print("")

    return [x,result]