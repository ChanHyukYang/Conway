import random
def rule(val,lis):
   accum = 0
   for i in lis:
      accum = accum + i
   if val == 1:
      if accum == 2 or accum == 3:
         return 1
      else:
         return 0
   if val ==0:
      if accum == 3:
         return 1
      else:
         return 0
class conway:
    def __init__(self, lists, spaces, value):
        self.store = []
        self.spaces = spaces
        self.lists = lists
        for i in range(0,lists,1):
            self.store = self.store + [[]]
        if value == 'zeros':
            for i in range(0,lists,1):
                for n in range(0,spaces,1):
                    self.store[i] = self.store[i] + [0]
        if value == 'random':
            for i in range(0,lists,1):
                for n in range(0,spaces,1):
                    self.store[i] = self.store[i] + [random.randint(0,1)]
    def getDisp(self):
        x = ''
        for i in self.store:
            counter = 1
            for n in i:
                if counter != len(i):
                    if n == 0:
                        x = x + ' '
                        counter = counter + 1
                    elif n == 1:
                        x = x + '*'
                        counter = counter + 1
                elif counter == len(i):
                    if n == 0:
                        x = x + ' ' + "\n"
                    elif n == 1:
                        x = x + '*' + "\n"
        return x
    def printDisp(self):
        try:
            print(self.getDisp())
            return True
        except:
            return False
    def setPos(self, row, col, val):
        if val != 0 and val != 1:
            return False
        self.store[row][col] = val
        return True
    def getNeighbours(self,row,col):
       # neighbours = []
        if row !=0 and row!=len(self.store)-1 and col!=0 and col!=self.spaces-1:
            neighbours = [[self.store[row-1][col-1]] + [self.store[row-1][col]] + [self.store[row-1][col+1] + self.store[row][col-1]] + [self.store[row][col+1]] + [self.store[row+1][col-1]] + [self.store[row+1][col]] + [self.store[row+1][col+1]]]
        elif row == 0 and col!=0 and col!=self.spaces-1:
            neighbours = [[self.store[len(self.store)-1][col-1]] + [self.store[len(self.store)-1][col]] + [self.store[len(self.store)-1][col+1]] + [self.store[row][col-1]] + [self.store[row][col+1]] + [self.store[row+1][col-1]] + [self.store[row+1][col]] + [self.store[row+1][col+1]]]
        elif row == len(self.store)-1 and col !=0 and col!=self.spaces-1:
            neighbours = [[self.store[row-1][col-1]] + [self.store[row-1][col]] + [self.store[row-1][col+1]] + [self.store[row][col-1]] + [self.store[row][col+1]] + [self.store[0][col-1]] + [self.store[0][col]] + [self.store[0][col+1]]]
        elif row != 0 and row != len(self.store)-1 and col == 0:
            neighbours = [[self.store[row-1][self.spaces-1]] + [self.store[row-1][col]] + [self.store[row-1][col+1]] + [self.store[row][self.spaces-1]] + [self.store[row][col+1]] + [self.store[row+1][self.spaces-1]] + [self.store[row+1][col]] + [self.store[row+1][col+1]]]
        elif row!=0 and row!=len(self.store)-1 and col == self.spaces-1:
            neighbours = [[self.store[row-1][col-1]] + [self.store[row-1][col]] + [self.store[row-1][0]] + [self.store[row][col-1]] + [self.store[row][0]] + [self.store[row+1][col-1]] + [self.store[row+1][col]] + [self.store[row+1][0]]]
        elif row == 0 and col == 0:
            neighbours = [[self.store[len(self.store)-1][self.spaces-1]] + [self.store[len(self.store)-1][col]] + [self.store[len(self.store)-1][col+1]] + [self.store[row][self.spaces-1]] + [self.store[row][col+1]] + [self.store[row+1][self.spaces-1]] + [self.store[row+1][col]] + [self.store[row+1][col+1]]]
        elif row == 0 and col == self.spaces-1:
            neighbours = [[self.store[len(self.store)-1][col-1]] + [self.store[len(self.store)-1][col]] + [self.store[len(self.store)-1][0]] + [self.store[row][col-1]] + [self.store[row][0]] + [self.store[row+1][col-1]] + [self.store[row+1][col]] + [self.store[row+1][0]]]
        elif row == len(self.store)-1 and col == 0:
            neighbours = [[self.store[row-1][self.spaces-1]] + [self.store[row-1][col]] + [self.store[row-1][col+1]] + [self.store[row][self.spaces-1]] + [self.store[row][col+1]] + [self.store[0][self.spaces-1]] + [self.store[0][col]] + [self.store[0][col+1]]]
        elif row == len(self.store)-1 and col == self.spaces-1:
            neighbours = [[self.store[row-1][col-1]] + [self.store[row-1][col]] + [self.store[row-1][0]] + [self.store[row][col-1]] + [self.store[row][0]] + [self.store[0][col-1]] + [self.store[0][col]] + [self.store[0][0]]]
        return neighbours[0]
    def evolve(self,rule):
       newstate = []
       for i in range(0,self.lists,1):
          newstate = newstate + [[]]
       for i in range(0,self.lists,1):
          for n in range(0,self.spaces,1):
             newstate[i] = newstate[i] + [0]
       for i in range(0,self.lists,1):
          for n in range(0,self.spaces,1):
             newstate[i][n] = rule(self.store[i][n],self.getNeighbours(i,n))
       self.store = list(newstate)
       return True
