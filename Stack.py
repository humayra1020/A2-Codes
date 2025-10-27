StackData = [0] * 10
stackpointer = 0

def PrintStack():
    global StackData
    global stackpointer
    print("Stack pointer is :",stackpointer)
    for i in range(10):
        print(StackData[i])

def Push(value):
    global StackData
    global stackpointer
    if stackpointer == 10:
        return(False)
    else:
        StackData[stackpointer] = value
        stackpointer += 1
        return(True)

for i in range(11):
    n = int(input("Enter a number :"))
    result = Push(n)
    if result:
        print("Successful")
    else:
        print("Failed")
    
PrintStack()

def pop():
    global StackData
    global stackpointer
    if stackpointer == 0:
        return -1
    else:
        stackpointer -= 1
        value = StackData[stackpointer]
        StackData[stackpointer] = ""
        return(value)
        

    
        

    
    
        