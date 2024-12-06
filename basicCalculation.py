import functions
import history

#add result as input
x=input("Enter your calculation +,-,*,/,(),^\n")

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

#gets rid of empty space
x=x.replace(" ","")
expressionArray=[]

lenOfX=len(x)

print(x)
print(lenOfX)
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
print(expressionArray)
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
        while oppStack and precedence[oppStack[-1]]>=precedence[i]:
            numQueue.append(oppStack.pop())
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
print(numQueue)

#goes through RPN array and operates
result=[]
for i in numQueue:
    if i.replace(".","").isdigit():
        result.append(i)
    else:
        result.append(functions.operation(result.pop(),result.pop(),i))
result=result[0]
print (result)

# history.appendHistory(x,result)