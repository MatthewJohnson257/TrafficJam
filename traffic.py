###############################################################################
#
# traffic.py
#
#
###############################################################################
import copy
import argparse
import sys
from state import State
from PriorityQueue import PriorityQueue



###############################################################################
#
#
###############################################################################
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
                        nextState = State(newBoard, -50, newState.doorColumn, newState)
                        if(usedHeuristic == 1):
                            nextState.hn = computeHeuristicOne(nextState)
                        else:
                            nextState.hn = computeHeuristicTwo(nextState)
                        nextState.fn = nextState.gn + nextState.hn
                        if(hashState(nextState) != False):
                            listOfPossibleStates.append(nextState)

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
                        nextState = State(newBoard, -50, newState.doorColumn, newState)
                        if(usedHeuristic == 1):
                            nextState.hn = computeHeuristicOne(nextState)
                        else:
                            nextState.hn = computeHeuristicTwo(nextState)
                        nextState.fn = nextState.gn + nextState.hn
                        if(hashState(nextState) != False):
                            listOfPossibleStates.append(nextState)
    
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
                        nextState = State(newBoard, -50, newState.doorColumn, newState)
                        if(usedHeuristic == 1):
                            nextState.hn = computeHeuristicOne(nextState)
                        else:
                            nextState.hn = computeHeuristicTwo(nextState)
                        nextState.fn = nextState.gn + nextState.hn
                        if(hashState(nextState) != False):
                            listOfPossibleStates.append(nextState)

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
                        nextState = State(newBoard, -50, newState.doorColumn, newState)
                        if(usedHeuristic == 1):
                            nextState.hn = computeHeuristicOne(nextState)
                        else:
                            nextState.hn = computeHeuristicTwo(nextState)
                        nextState.fn = nextState.gn + nextState.hn
                        if(hashState(nextState) != False):
                            listOfPossibleStates.append(nextState)


    return(listOfPossibleStates)


    
###############################################################################
#
#
###############################################################################
def computeHeuristicOne(newState):
    blockingCarCount = 0
    for i in range(0,newState.numColumns):       
        if(newState.board[i][newState.doorColumn] == 'R'):
            break
        elif(newState.board[i][newState.doorColumn] != ' '):
            blockingCarCount = blockingCarCount + 1
    return blockingCarCount 
            



###############################################################################
#
#
###############################################################################
def computeHeuristicTwo(newState):
    blockingCarCount = 0
    spaceFromExit = 0
    for i in range(0,newState.numColumns):
        #If we reach the red car going down       
        if(newState.board[i][newState.doorColumn] == 'R'):
            break
        #If we reach a non-empty space in front of red car, i.e. a car or truck
        elif(newState.board[i][newState.doorColumn] != ' '):
            #If the red car is in the last column and cars will be blocked on right side
            if(newState.doorColumn == newState.numColumns - 1):
                #Start from the right and see if there is a car blocking the blocking car
                for j in range(newState.doorColumn -1, 0, -1):
                    #If there is no car to the left of the blocking car
                    if(newState.board[i][j] == ' '):
                        blockingCarCount = blockingCarCount + 1
                        break
                    #If there is a car to the left of the blocking car
                    elif(newState.board[i][j] != newState.board[i][j+1]):
                        blockingCarCount = blockingCarCount + 2
                        break
            #If the red car is in the first column and cars will be blocked on the left
            elif(newState.doorColumn == 0):
                #Start from the right and see if there is a car blocking the blocking car
                for j in range(0, newState.doorColumn -1):
                    #If there is no car to the left of the blocking car
                    if(newState.board[i][j] == ' '):
                        blockingCarCount = blockingCarCount + 1
                        break
                    #If there is a car to the left of the blocking car
                    elif(newState.board[i][j] != newState.board[i][j-1]):
                        blockingCarCount = blockingCarCount + 2
                        break
            else:
                #Start from the current column and check both forward and backward
                for j in range(0, newState.doorColumn):
                    #If there is no car to either the left or right of the blocking car
                    if(newState.board[i][j] == ' ' or newState.board[i][-j] == ' '):
                        blockingCarCount = blockingCarCount + 1
                        break
                    #If there is a car to either the left or right of the blocking car
                    elif(newState.board[i][j] != newState.board[i][j-1] or newState.board[i][-j] != newState.board[i][-j + 1]):
                        blockingCarCount = blockingCarCount + 2
                        break

    #Add the number of blank spaces between the red car and the exit
    for i in range(0,newState.numColumns):       
        if(newState.board[i][newState.doorColumn] == 'R'):
            break
        # elif(newState.board[i][newState.doorColumn] == ' '):
        #     spaceFromExit = spaceFromExit + 1
        else:
            spaceFromExit = spaceFromExit + 1


    return blockingCarCount + spaceFromExit





###############################################################################
#
#
###############################################################################
def checkGoalTest(currentState):
    if(currentState.board[0][currentState.doorColumn] == 'R'):
        return(True)
    else:
        return(False)




###############################################################################
#
#
###############################################################################
def hashState(currentState):
    tempBoard = copy.deepcopy(currentState.board)
    # print(tempBoard)
    tempString = ""
    for i in range(0, len(tempBoard)):
        for j in range(0, len(tempBoard[0])):
            tempString = tempString + tempBoard[i][j]
    tempString2 = copy.deepcopy(tempString)
    tempString = tempString + str(currentState.fn)
    tempString2 = tempString2 + str(currentState.fn - 2)
    tempString = tempString + str(currentState.gn)
    tempString2 = tempString2 + str(currentState.gn - 2)
    tempString = tempString + str(currentState.hn)
    tempString2 = tempString2 + str(currentState.hn)
    tempString = tempString + '.'
    tempString2 = tempString2 + '.'

    # if the state has already been visited
    if (tempString in listOfVisitedStates or tempString2 in listOfVisitedStates):
        return(False)
    else:
        listOfVisitedStates.append(tempString)


###############################################################################
#
#
###############################################################################
def printPath(goalState):
    path = [goalState]
    tempState = goalState
    while(tempState.parentState != None):
        path.append(tempState.parentState)
        tempState = tempState.parentState

    for x in reversed(path):
        print("-------------------------")
        # print(computeHeuristicThree(x))
        x.printBoard()
        # print(x.board)



###############################################################################
#                                                                             #
#                                Global Scope                                 #
#                                                                             #
###############################################################################

parser = argparse.ArgumentParser()
parser.add_argument('Arguments', metavar='N', type=int, nargs='+')
arguments = parser.parse_args()

if(len(arguments.Arguments) != 2):
    sys.exit("    Error: Incorrect number of command line arguments supplied; 2 needed")
if(arguments.Arguments[0] < 1 or arguments.Arguments[0] > 3):
    sys.exit("    Error: Invalid value for first command line argument; must be in range(1,3)")
if(arguments.Arguments[1] < 1 or arguments.Arguments[1] > 2):
    sys.exit("    Error: Invalid value for second command line argument; must be in range(1,2)")

usedPuzzle = arguments.Arguments[0]
usedHeuristic = arguments.Arguments[1]



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

stateA = State(initialStateA, 3, 5, None)
stateB = State(initialStateB, 3, 4, None)
stateC = State(initialStateC, 2, 5, None)

listOfVisitedStates = []

pq = PriorityQueue()

statesTested = 0



if(usedPuzzle == 1):
    pq.add_state(stateA, 3)
elif(usedPuzzle == 2):
    pq.add_state(stateB, 3)
elif(usedPuzzle == 3):
    pq.add_state(stateC, 2)

goalNotReached = False
while (not goalNotReached):
    poppedState = pq.pop_state()
    statesTested = statesTested + 1
    goalNotReached = checkGoalTest(poppedState)
    if(goalNotReached):
        printPath(poppedState)
        print("Total path cost: ",poppedState.fn)
        print("Number of states tested: ",statesTested)
        break
    newList = findPossibleStates(poppedState)
    for x in newList:
        pq.add_state(x,x.fn)




