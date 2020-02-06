import itertools  
import heapq

class PriorityQueue():
    pq = []                         # list of entries arranged in a heap
    entry_finder = {}               # mapping of tasks to entries
    REMOVED = '<removed-state>'      # placeholder for a removed task
    counter = itertools.count()     # unique sequence count

    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.REMOVED = '<removed-state>'
        self.counter = itertools.count()


    def add_state(self, state, priority=0):
        'Add a new state or update the priority of an existing state'
        if state in self.entry_finder:
            print("Here")
            if(state.fn <= priority):
                print("AHHHHHH")
                return
            print("OHHHHHH")
            self.remove_state(state)
        count = next(self.counter)
        entry = [priority, count, state]
        self.entry_finder[state] = entry
        heapq.heappush(self.pq, entry)

    def remove_state(self, state):
        'Mark an existing state as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(state)
        entry[-1] = self.REMOVED

    def pop_state(self):
        'Remove and return the lowest priority state. Raise KeyError if empty.'
        while self.pq:
            priority, count, state = heapq.heappop(self.pq)
            if state is not self.REMOVED:
                del self.entry_finder[state]
                return state
        raise KeyError('pop from an empty priority queue')