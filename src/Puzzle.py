import copy
class Puzzle :
    
    def __init__(self, thePuzzle, depth):
        self.puzzle = thePuzzle
        self.depth = depth
        self.cost = 0
        self.lastMove = ""
        self.TotalMove = []

    def printPuzzle(self):
        print('-'*29)
        for i in range(4):
            for j in range(4):
                if(self.puzzle[i][j] >= 10):
                    if(j == 3):
                        if(self.puzzle[i][j] == 16):
                            print("|      |", end='\n')
                        else :
                            print("| " , self.puzzle[i][j]," |", end='\n')
                    else:
                        if(self.puzzle[i][j] == 16):
                            print("|      ", end='')
                        else :
                            print("| " , self.puzzle[i][j]," ", end='')
                else :
                    if(j == 3):
                        print("| ", self.puzzle[i][j], "  |", end='\n')
                    else: 
                        print("| ", self.puzzle[i][j], "  ", end='')

            print('-'*29)

    def findEmptySlot(self):
        for i in range(4):
            for j in range(4):
                if(self.puzzle[i][j] == 16):
                    return (i,j)


    def isThereAreState(self, dict, matriks):
        for i in range(len(dict)):
            if(dict[i] == matriks):
                return True
        return False

    def move(self, row, column, move, dict):
        emptyRow, emptyCol = self.findEmptySlot()
        
        if(emptyRow+row>=0 and emptyRow+row<=3 and emptyCol+column>=0 and emptyCol+column<=3):
            newPuzzle = copy.deepcopy(self)
            newPuzzle.depth +=1
            newPuzzle.lastMove = move
            newPuzzle.TotalMove.append(move)
            newPuzzle.puzzle[emptyRow][emptyCol], newPuzzle.puzzle[emptyRow+row][emptyCol+column] = newPuzzle.puzzle[emptyRow+row][emptyCol+column], newPuzzle.puzzle[emptyRow][emptyCol]
            if(not self.isThereAreState(dict, newPuzzle.puzzle)):
                dict[len(dict)] = newPuzzle.puzzle
                return newPuzzle
            else:
                return None
        else:
            return None

    def funcG(self):
        finalState = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        costG = 0

        for i in range(4):
            for j in range(4) :
                if(self.puzzle[i][j] != finalState[i][j] and self.puzzle[i][j] != 16):
                    costG += 1

        return costG

    def setCost(self):
        costG = self.funcG()
        self.cost = costG + self.depth

    def isGoalState(self):
        finalState = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13, 14, 15, 16]]
        return self.puzzle == finalState

    def printAll(self, totalMove):
        print("\nInitial State :")
        self.printPuzzle()

        moveUnit = [(-1,0), (0,-1), (1,0),(0,1)]

        for i in range(len(totalMove)):
            moveIdx = 0
            if(totalMove[i] == "Up"):
                moveIdx = 0
            elif(totalMove[i] == "Left"):
                moveIdx = 1
            elif(totalMove[i] == "Down"):
                moveIdx = 2
            elif(totalMove[i] == "Right"):
                moveIdx = 3
            
            row, col = moveUnit[moveIdx]
            emptyRow, emptyCol = self.findEmptySlot()
            self.puzzle[emptyRow][emptyCol], self.puzzle[emptyRow+row][emptyCol+col] = self.puzzle[emptyRow+row][emptyCol+col], self.puzzle[emptyRow][emptyCol]

            print("\nGerakan", i+1, ":",totalMove[i])
            self.printPuzzle()

        print("\nPuzzle Solved")
        print("The Step : ", end='')
        for i in range(len(totalMove)):
            print(totalMove[i], end=' ')
        print("\nStep count :", len(totalMove))
    