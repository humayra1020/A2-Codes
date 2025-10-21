QueueArray = [""]*10 #DECLARE QueueArray : ARRAY [0:9] OF STRING

global HeadPointer
global TailPointer
global NumberOfItems

HeadPointer = 0 #INTEGER
TailPointer = 0 #INTEGER
NumberOfItems = 0 #INTEGER

#Cannot pass parameters by reference so have decleared them as global variables
def Enqueue(Data):
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberOfItems
    
    if NumberOfItems >= 10:
       return False
    QueueArray[TailPointer] = Data
    if TailPointer == 9:
        TailPointer = 0
    else:
        TailPointer += 1
    NumberOfItems += 1
    return True

def Dequeue():
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberOfItems
    if NumberOfItems == 0:
        return False
    item = QueueArray[HeadPointer]
    HeadPointer += 1
    if HeadPointer > 9:
        HeadPointer = 0
    NumberOfItems -= 1
    return item

Enqueue("A")
Enqueue("B")
Enqueue("C")
Enqueue("D")
Enqueue("E")
Enqueue("F")
Enqueue("G")
Enqueue("H")
Enqueue("I")
Enqueue("J")    
Dequeue()
Dequeue()
Enqueue("L")
Enqueue("M")

print(QueueArray)
print("NUMBER OF ITEMS :",NumberOfItems)
print("HEAD POINTER :",HeadPointer)
print("TAIL POINTER :",TailPointer)

    


    
    

    



