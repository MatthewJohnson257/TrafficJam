# Traffic
import copy
from state import State


initialStateA = [[' ', ' ', ' ', 'A', 'B', 'B'],
                 [' ', ' ', ' ', 'A', 'C', 'C'],
                 ['D', 'E', 'E', 'E', 'F', 'F'],
                 ['D', ' ', ' ', ' ', ' ', 'R'],
                 [' ', ' ', 'G', 'G', 'G', 'R'],
                 [' ', ' ', ' ', ' ', ' ', ' ']]

initialStateB = [['A', 'B', 'C', 'D', 'D', 'D'],
                 ['A', 'B', 'C', 'E', 'E', 'E'],
                 ['A', 'B', 'F', 'F', 'G', 'G'],
                 ['H', 'H', ' ', ' ', 'R', ' '],
                 [' ', ' ', ' ', ' ', 'R', ' '],
                 [' ', ' ', 'I', 'I', ' ', ' ']]

initialStateC = [[' ', ' ', 'A', 'B', 'B', 'B'],
                 [' ', ' ', 'A', 'C', 'D', 'D'],
                 [' ', 'E', 'A', 'C', ' ', 'R'],
                 ['G', 'E', 'F', 'F', 'F', 'R'],
                 ['G', 'E', ' ', 'H', 'H', 'H'],
                 ['G', ' ', ' ', ' ', ' ', ' ']]

stateA = State(initialStateA, -1, 5)
stateB = State(initialStateB, -1, 4)
stateC = State(initialStateC, -1, 5)


def findPossibleStates(newState):
    currentBoard = copy.deepcopy(newState.board)
    listOfPossibleStates = []

    for i in range(0,newState.numRows):
        for j in range(0,newState.numColumns):
            if(currentBoard[i][j] == ' '):
                # check if a vehicle can move right into this space
                if(j > 1):
                    if(currentBoard[i][j-1] != ' ' and (currentBoard[i][j-1] == currentBoard[i][j-2])):
                        newBoard = copy.deepcopy(currentBoard)
                        # for trucks
                        if(j > 2 and currentBoard[i][j-1] == currentBoard[i][j-3]):
                            newBoard[i][j] = newBoard[i][j-1]
                            newBoard[i][j-3] = ' '
                        # for cars
                        else:
                            newBoard[i][j] = newBoard[i][j-1]
                            newBoard[i][j-2] = ' '
                        newState = State(newBoard, 5, newState.doorColumn)
                        listOfPossibleStates.append(newState)

                # check if a vehicle can move left into this space
                if(j < newState.numColumns - 2):
                    if(currentBoard[i][j+1] != ' ' and (currentBoard[i][j+1] == currentBoard[i][j+2])):
                        newBoard = copy.deepcopy(currentBoard)
                        # for trucks
                        if(j < 3 and currentBoard[i][j+1] == currentBoard[i][j+3]):
                            newBoard[i][j] = newBoard[i][j+1]
                            newBoard[i][j+3] = ' '
                        # for cars
                        else:
                            newBoard[i][j] = newBoard[i][j+1]
                            newBoard[i][j+2] = ' '
                        newState = State(newBoard, 5, newState.doorColumn)
                        listOfPossibleStates.append(newState)
    
                # check if a vehicle can move down into this space
                if(i > 1):
                    if(currentBoard[i-1][j] != ' ' and (currentBoard[i-1][j] == currentBoard[i-2][j])):
                        newBoard = copy.deepcopy(currentBoard)
                        # for trucks
                        if(i > 2 and currentBoard[i-1][j] == currentBoard[i-3][j]):
                            newBoard[i][j] = newBoard[i-1][j]
                            newBoard[i-3][j] = ' '
                        # for cars
                        else:
                            newBoard[i][j] = newBoard[i-1][j]
                            newBoard[i-2][j] = ' '
                        newState = State(newBoard, 5, newState.doorColumn)
                        listOfPossibleStates.append(newState)

                # check if a vehicle can move up into this space
                if(i < newState.numRows - 2):
                    if(currentBoard[i+1][j] != ' ' and (currentBoard[i+1][j] == currentBoard[i+2][j])):
                        newBoard = copy.deepcopy(currentBoard)
                        # for trucks
                        if(i < 3 and currentBoard[i+1][j] == currentBoard[i+3][j]):
                            newBoard[i][j] = newBoard[i+1][j]
                            newBoard[i+3][j] = ' '
                        # for cars
                        else:
                            newBoard[i][j] = newBoard[i+1][j]
                            newBoard[i+2][j] = ' '
                        newState = State(newBoard, 5, newState.doorColumn)
                        listOfPossibleStates.append(newState)

    
    for x in listOfPossibleStates:
        print("-----------------------")
        print("length: ", len(listOfPossibleStates))
        x.printBoard()
        print("-----------------------")

    return(listOfPossibleStates)


    

def computeHeuristicOne(newState):
    blockingCarCount = 0
    for i in range(0,newState.numColumns):       
        if(newState.board[i][newState.doorColumn] == 'R'):
            break
        elif(newState.board[i][newState.doorColumn] != ' '):
            blockingCarCount = blockingCarCount + 1
    return blockingCarCount 
            

#print(computeHeuristicOne(stateA))
#print(computeHeuristicOne(stateB))
#print(computeHeuristicOne(stateC))

findPossibleStates(stateC)




























































####### Logic Order ########
# 1. Pop from frontier, which is priority queue
# 2. Discover valid move(s) for a car
# 3. Check if that state has already been visited (hashing)
# 4. If not, calculate A* heuristic stuff
# 5. Add to frontier, which is a priority queue
# 

###### Need to figure out ########
# 1. How to store path
# 2. How to check if a move is valid
# 3. Create object for state

####### Needed for state object ######
# 1. 2d array of char
# 2. column of door
# 3. heuristic f(n)

####### TO DO LIST #######
# 1. Keep track of path
# 2. Dictionary for visited nodes
# 3. Correct implementation of total heuristic (need g(n) part)
#    - gn is an instance variable in state - implement its functionality
# 4. Goal testing
#    - if red car is at index [0][doorColumn]
# 5. Keeping track of door column for realsies  (Edit: COMPLETE! I think)
# 6. Keep track of final path length
# 7. Keep track of number of states visited