###############################################################################
#
# Implementation of a priority queue in Python; used to determine next visited
# node/State in for the traffic puzzle
#
###############################################################################

import itertools  
import heapq
import copy

class PriorityQueue():
    pq = []                         # list of entries arranged in a heap
    entry_finder = {}               # mapping of tasks to entries
    REMOVED = '<removed-state>'      # placeholder for a removed task
    counter = itertools.count()     # unique sequence count
    listOfVisited = []

    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.REMOVED = '<removed-state>'
        self.counter = itertools.count()


    def add_state(self, state, priority=0):
        #Add a new state or update the priority of an existing state
        if state in self.entry_finder:
            if(state.fn <= priority):
                return
            self.remove_state(state)
        count = next(self.counter)
        entry = [priority, count, state]
        self.entry_finder[state] = entry
        heapq.heappush(self.pq, entry)

    def remove_state(self, state):
        #Mark an existing state as REMOVED.  Raise KeyError if not found.
        entry = self.entry_finder.pop(state)
        entry[-1] = self.REMOVED


    def hashState(self, currentState):
        # used to verify if a state has already been in the priority queue
        tempBoard = copy.deepcopy(currentState.board)
        tempString = ""
        for i in range(0, len(tempBoard)):
            for j in range(0, len(tempBoard[0])):
                tempString = tempString + tempBoard[i][j]
        tempString = tempString + '.'

        if(tempString in self.listOfVisited):
            return(False)
        else:
            self.listOfVisited.append(tempString)
            return(True)


    def pop_state(self):
        #Remove and return the lowest priority state. Raise KeyError if empty.
        while self.pq:
            priority, count, state = heapq.heappop(self.pq)
            if state is not self.REMOVED:
                del self.entry_finder[state]
                if(self.hashState(state) != False):
                    return state
                else:
                    return self.pop_state()
        raise KeyError('pop from an empty priority queue')
