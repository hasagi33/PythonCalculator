import math
import sys
from platform import system
from unittest import case

import calculations
import functions
import history

x = 0

while x != "4":
    print("Calculator Menu: \n"
          "1. Perform Basic Calculation \n"
          "2. Calculate Square Root\n"
          "3. View History\n"
          "4. Exit\n")
    x = input("Choose an option:")
    match x:
        case "1":
            while True:
                calculation_input = input("Enter your calculation +,-,*,/,(),^\nWrite exit or leave empty to go back: ")
                # calculated = calculations.calculate(calculation_input)
                # print("Result:", calculated[1])
                #Enable back when fully working

                try:
                    calculated = calculations.calculate(calculation_input)
                except ZeroDivisionError:
                    print("Error, cant divide by zero")
                except (NameError, IndexError) as e:
                    print("Error, bad expression")
                except TypeError:
                    print("Error, no letters allowed in expression")
                else:
                    if calculated[0] == "exit":
                        break
                    print("Result:", calculated[1])
                    history.appendHistory(calculated[0], calculated[1])

        case "2":
            while True:
                calculation_input = input("Enter number to square root\nWrite exit to go back: ")
                try:
                    calculated = calculations.sqrt(calculation_input)
                except ValueError as ve:
                    if ve.args[0] == 'math domain error':
                        print("Error, cant square root negative number")
                    if ve.args[0][:32] == "could not convert string to float: "[:32]:
                        print("Error, cant square root characters")
                else:
                    if calculated[1] == "exit":
                        break
                    print("Result:", calculated[1])
                    history.appendHistory("√" + str(calculated[0]), calculated[1])

        case "3":
            history.viewHistory()
        case "4":
            pass
