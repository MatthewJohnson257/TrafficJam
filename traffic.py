# Traffic


initialStateA = [[' ', ' ', ' ', 'A', 'B', 'B'],
                 [' ', ' ', ' ', 'A', 'C', 'C'].
                 ['D', 'E', 'E', 'E', 'F', 'F'],
                 ['D', ' ', ' ', ' ', ' ', 'R'],
                 [' ', ' ', 'G', 'G', 'G', 'R'],
                 [' ', ' ', ' ', ' ', ' ', ' ']]

initialStateB = [['A', 'B', 'C', 'D', 'D', 'D'],
                 ['A', 'B', 'C', 'E', 'E', 'E'].
                 ['A', 'B', 'F', 'F', 'G', 'G'],
                 ['H', 'H', ' ', ' ', 'R', ' '],
                 [' ', ' ', ' ', ' ', 'R', ' '],
                 [' ', ' ', 'I', 'I', ' ', ' ']]

initialStateC = [[' ', ' ', 'A', 'B', 'B', 'B'],
                 [' ', ' ', 'A', 'C', 'D', 'D'].
                 [' ', 'E', 'A', 'C', ' ', 'R'],
                 ['G', 'E', 'F', 'F', 'F', 'R'],
                 ['G', 'E', ' ', 'H', 'H', 'H'],
                 ['G', ' ', ' ', ' ', ' ', ' ']]


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
# 3. heuristic f(n) = 1 

