import math
import re

import functions

# PEMDAS
#add fact!
precedence = {
    "^": 4,
    "*": 3,
    "/": 3,
    "+": 2,
    "-": 2,
    "(": 0,
    ")": 0
}


def sqrt(calculation_input):
    if calculation_input == "exit":
        return ["exit", "exit"]
    result = math.sqrt(float(calculation_input))
    return [calculation_input, result]


def calculate(calculation_input):
    # to do: add result as input, maybe !

    if calculation_input == "exit" or calculation_input == "":
        return ["exit", "exit"]
    x = calculation_input.replace(" ", "")
    if x != re.sub('[a-z]', '', x):
        raise TypeError


    expression_array = functions.string_to_list(x)

    opp_stack = []
    num_queue = []

    # converts expression array into reverse polish notation (postfix)
    for i in expression_array:
        if i.replace(".", "").isdigit():
            num_queue.append(i)
        elif i == "(":
            opp_stack.append(i)
        elif i == ")":
            while opp_stack:
                if opp_stack[-1] != "(":
                    num_queue.append(opp_stack.pop())
                else:
                    opp_stack.pop()
                    break
        elif i == "^":
            opp_stack.append(i)
        elif i == "*" or i == "/":
            while opp_stack and precedence[opp_stack[-1]] >= precedence[i]:
                num_queue.append(opp_stack.pop())
            opp_stack.append(i)
        elif i == "+" or i == "-":
            while opp_stack and precedence[opp_stack[-1]] >= precedence[i]:
                num_queue.append(opp_stack.pop())
            opp_stack.append(i)

    for i in range(len(opp_stack)):
        num_queue.append(opp_stack.pop())

    # goes through RPN array and operates
    result = []
    for i in num_queue:
        if i.replace(".", "").isdigit():
            result.append(i)
        else:
            result.append(functions.operation(result.pop(), result.pop(), i))
    if len(result) > 1:
        raise NameError
    result = result[0]

    return [x, result]


