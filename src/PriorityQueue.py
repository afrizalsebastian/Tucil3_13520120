#Class PriorityQueue

class PriorityQueue :

    def __init__(self, prioFunc) :
        self.buffer = []
        self.prioFunc = prioFunc

    def isEmpty(self):
        return len(self.buffer) == 0

    def first(self) :
        return self.buffer[0]

    def enqueue(self, puzzle):
        idx = 0
        found = False

        while(not found and idx < len(self.buffer)) :
            if(self.prioFunc(puzzle, self.buffer[idx])) :
                found = True
            else :
                idx +=1
        
        self.buffer.insert(idx, puzzle)

    def dequeu(self):
        self.buffer.pop(0)


