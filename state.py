###############################################################################
#
# Keeps track of a state/node in for the traffic puzzle.  Includes information
# such as the board (where all the cars are), the column of the door, and the
# f(n), g(n), and h(n) values used in the A* algorithm
#
###############################################################################

class State():
    fn = 0          # f(n)
    gn = 0          # g(n)
    numRows = 0
    numColumns = 0
    doorColumn = 0
    parentState = None      # previous state in transition model

    def __init__(self, board, fn, doorColumn, parentState):
        self.board = board      # 2d array of char representing the traffic grid
        self.fn = fn
        self.doorColumn = doorColumn
        self.numRows = len(board)
        self.numColumns = len(board[0])
        self.parentState = parentState
        if(self.parentState != None):
            self.gn = parentState.gn + 1

    # used to neatly print the values of the board
    def printBoard(self):
        for i in range(0,self.numRows):
            for j in range(0, self.numColumns):
                print(self.board[i][j], end = ' ')
            print()
