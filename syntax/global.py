#Global variable explanation
thisIsAGlobalVariable = "Hi im Global"


def myfunc():
    global globalVariable
    globalVariable = "Global even inside function"
    insideFunctionVariable = "Inside Function"
    print("VARIABLE RESULT ", thisIsAGlobalVariable, insideFunctionVariable)

myfunc()
print("Printing outside a function ",thisIsAGlobalVariable, globalVariable)