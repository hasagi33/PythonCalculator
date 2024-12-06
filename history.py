import json
def appendHistory(expression,result):

    with open("history.json","r") as openfile:
        historyObj=json.load(openfile)
    historyObj2=[
        {
            "expression":expression,
            "result":result
        }
    ]
    print(historyObj2)
    historyObj=historyObj+historyObj2
    with open("history.json","w") as outfile:
        json.dump(historyObj,outfile)