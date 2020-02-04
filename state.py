class State():
    board = [[' ' * 6] * 6]
    fn = 0
    doorColumn = 0

    def __init__(self, board, fn, doorColumn):
        self.board = board
        self.fn = fn
        self.doorColumn = doorColumn

    