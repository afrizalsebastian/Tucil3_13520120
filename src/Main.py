import timeit
from PriorityQueue import PriorityQueue
from Puzzle import Puzzle


def make1Dmatriks(matriks):
    idx = 0
    returnMat = [0 for i in range(16)]
    for i in range(4):
        for j in range(4) :
            returnMat[idx] = matriks[i][j]
            idx+=1
    return returnMat

def kurangI(matriks) :
    temp = make1Dmatriks(matriks)
    kurang = 0
    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            if(temp[i] > temp[j]):
                kurang +=1
    return kurang

def emptySlot(matriks):
    for i in range(4):
        for j in range(4):
            if(matriks[i][j] == 16):
                if(i+j) % 2 == 1:
                    return 1
                else:
                    return 0


def isSolveAble(matriks) :
    kurangi = kurangI(matriks)
    empty = emptySlot(matriks)
    return (kurangi + empty)%2 == 0


def isThereAreState(dict, matriks):
    for i in range(len(dict)):
        if(dict[i] == matriks):
            return True
    return False

if __name__ == '__main__' :
    
    print("--- Selamat Datang ---")
    print("---------Menu---------")
    print("1. Masukan Puzzle Melalui Konsol")
    print("2. Masukan Puzzle Melalui File")
    print("Else. Exit")
    print(">> ", end='')
    menu = int(input(""))

    initialState = [[0 for j in range(4)] for i in range(4)]
    if(menu == 1):
        print("Bagian Kosong diganti dengan '-' ")
        print("Masukkan Puzzle : ")
        for i in range(4): 
            value = input("")
            temp = ""
            j = 0
            for k in range(len(value)):
                if(value[k] != ' '):
                    temp += value[k]
                else:
                    if(temp == '-'):
                        initialState[i][j] = 16
                        temp = ""
                        j+=1
                    else:
                        intTemp = int(temp)
                        initialState[i][j] = intTemp
                        temp = ""
                        j += 1
                
                if(k == len(value)-1):
                    if(temp == '-'):
                        initialState[i][j] = 16
                        temp = ""
                        j+=1
                    else:
                        intTemp = int(temp)
                        initialState[i][j] = intTemp
                        temp = ""
                        j += 1
                                  
    elif(menu == 2):
        path = "../test/"
        fileName = input("Masukkan nama file : ")
        path += fileName

        file = open(path, "r")
        line = file.readlines()
        for i in range(len(line)):
            value = line[i]
            temp = ""
            j = 0
            for k in range(len(value)):
                if(value[k] != ' '):
                    temp += value[k]
                else:
                    if(temp == '-'):
                        initialState[i][j] = 16
                        temp = ""
                        j+=1
                    else:
                        intTemp = int(temp)
                        initialState[i][j] = intTemp
                        temp = ""
                        j += 1
                
                if(k == len(value)-1):
                    if(temp == '-'):
                        initialState[i][j] = 16
                        temp = ""
                        j+=1
                    else:
                        intTemp = int(temp)
                        initialState[i][j] = intTemp
                        temp = ""
                        j += 1
        file.close()
    else:
        exit()

    startTime = timeit.default_timer()
    if(isSolveAble(initialState)):
        print("Puzzle is solveable")
        print("Kurang(i) = ", kurangI(initialState)+emptySlot(initialState))
        pQueue = PriorityQueue(lambda x,y : x.cost <= y.cost)

        moveUnit = [(-1,0), (0,-1), (1,0),(0,1)]
        moveName = ["Up", "Left", "Down", "Right"]
        moveOpposite = ["Down", "Right", "Up", "Left"]

        initialPuzzle = Puzzle(initialState, 0)
        pQueue.enqueue(initialPuzzle)

        stateTracking = {0 : initialPuzzle.puzzle}

        finished = False
        nodeCount = 0
        print("\nSolving.....")
        while(not pQueue.isEmpty() and not finished):
            if(pQueue.first().isGoalState()):
                finished = True
            else:
                current = pQueue.first()
                pQueue.dequeu()
                for i in range(len(moveName)):
                    if(current.lastMove == ""):
                        row, col = moveUnit[i]

                        nextPuzzle = current.move(row, col, moveName[i])
                        if(nextPuzzle != None) :
                                nextPuzzle.setCost()

                                pQueue.enqueue(nextPuzzle)

                                nodeCount+=1
            

                    else:
                        lastMove = current.lastMove
                        idxMove = 0
                        found = False

                        while(not found and idxMove < len(moveName)):
                            if(moveName[idxMove] == lastMove):
                                found = True
                            else:
                                idxMove +=1
                        
                        if(idxMove != lastMove):
                            row, col = moveUnit[i]

                            nextPuzzle = current.move(row, col, moveName[i])
                            if(nextPuzzle != None) :
                                nextPuzzle.setCost()

                                if(not isThereAreState(stateTracking, nextPuzzle.puzzle)):
                                    pQueue.enqueue(nextPuzzle)

                                    nodeCount+=1
                                    startTime
                                    stateTracking[len(stateTracking)] = nextPuzzle.puzzle


        initialPuzzle.printAll(pQueue.first().TotalMove)
        print("Raised Node Count : ", nodeCount)
    else:
        print("Puzzle is unsolveable")
    stopTime = timeit.default_timer()

    timeExecustion = stopTime - startTime
    print("Execution Time :", timeExecustion, "seconds")
