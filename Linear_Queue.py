#LINEAR QUEUE
# DECLARE Names : ARRAY [0:9] OF STRING

Names = [""] * 10
HeadPointer = 0 #INTEGER
TailPointer = 0 #INTEGER

def Enqueue(Data):
    global Names
    global HeadPointer
    global TailPointer
    
    if TailPointer < 10:
        Names[TailPointer] = Data
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0
    else:
        print("Queue is Full")
        
def Dequeue():
    global Names
    global HeadPointer
    global TailPointer
    if HeadPointer == -1:
        print("Queue is Empty")
    else:
        item = Names[HeadPointer] 
        HeadPointer += 1
        print(item)
        
    if HeadPointer == TailPointer:
        HeadPointer = -1
        TailPointer = 0
        

Enqueue("Humayra")
Enqueue("Muri")
Enqueue("Humayra")
Dequeue()
Dequeue()
print(Names,HeadPointer,TailPointer)

