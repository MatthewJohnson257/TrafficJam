class State():
    board = [[' ' * 6] * 6]
    fn = 0
    gn = 0
    hn = 0
    numRows = 0
    numColumns = 0
    doorColumn = 0
    parentState = None
    # parent and child needed  STUB STuB stuB STUB

    def __init__(self, board, hn, doorColumn, parentState):
        self.board = board
        self.doorColumn = doorColumn
        self.numRows = len(board)
        self.numColumns = len(board[0])
        self.parentState = parentState
        if(self.parentState != None):
            self.gn = parentState.gn + 1
        else:
            self.gn = 0
        self.fn = self.gn + self.hn

    
    def printBoard(self):
        for i in range(0,6):
            print(self.board[i][0], ' ', self.board[i][1], ' ',
                  self.board[i][2], ' ', self.board[i][3], ' ',
                  self.board[i][4], ' ', self.board[i][5], ' ')
© 2020 GitHub, Inc.