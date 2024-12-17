import json
import os

historyPath = "history.json"


def appendHistory(expression, result):
    if os.path.exists(historyPath):
        try:
            with open(historyPath, "r") as openfile:
                historyObj = json.load(openfile)
        except:
            historyObj = []
    else:
        historyObj = []

    if not bool(historyObj):
        historyObj = []

    historyObj.append({"expression": expression,
                       "result": result})

    with open(historyPath, "w") as outfile:
        json.dump(historyObj, outfile)


def viewHistory():
    if os.path.exists(historyPath):
        print("\n")
        try:
            with open(historyPath, "r") as openfile:
                historyObj = json.load(openfile)
            for i, item in enumerate(historyObj):
                print(i + 1, ":", item['expression'], "=", item['result'])
        except:
            print("Object is empty")
