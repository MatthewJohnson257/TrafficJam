class State():
    board = [[' ' * 6] * 6]
    fn = 0
    doorColumn = 0
    # parent and child needed  STUB STuB stuB STUB

    def __init__(self, board, fn, doorColumn):
        self.board = board
        self.fn = fn
        self.doorColumn = doorColumn

    
    def printBoard(self):
        for i in range(0,6):
            print(self.board[i][0], ' ', self.board[i][1], ' ',
                  self.board[i][2], ' ', self.board[i][3], ' ',
                  self.board[i][4], ' ', self.board[i][5], ' ')
