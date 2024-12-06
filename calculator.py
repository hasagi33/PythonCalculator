from unittest import case

import basicCalculation
import history

print("Calculator Menu: \n"
      "1. Perform Basic Calculation \n"
      "2. Calculate Square Root\n"  
      "3. View History\n"
      "4. Exit\n")
x = input("Choose an option:")

while x != "4":
      match x:
            case "1":
                  while True:
                        try:
                              calculated=basicCalculation.calculate()
                              if calculated[0]=="exit":
                                    break
                              history.appendHistory(calculated[0],calculated[1])
                        except ZeroDivisionError:
                              print("Error, cant divide by zero")
                        except (NameError,IndexError) as e:
                              print("Error, bad expression")
                        except TypeError:
                              print("Error, no letters allowed in expression")
            case "2":
                  while True:
                        try:
                              calculated=basicCalculation.sqrt()
                              if calculated[1] == "exit":
                                    break
                              history.appendHistory("√"+str(calculated[0]),calculated[1])
                        except ValueError as ve:
                              if ve.args[0]=='math domain error':
                                    print("Error, cant square root negative number")
                              if ve.args[0][:32]=="could not convert string to float: "[:32]:
                                    print("Error, cant square root characters")
            case "3":
                  history.viewHistory()
            case "4":
                  pass
      print("\nCalculator Menu: \n"
            "1. Perform Basic Calculation \n"
            "2. Calculate Square Root\n"
            "3. View History\n"
            "4. Exit")
      x = input("Choose an option:")