Usage:

Navigate inside the traffic directory.  To run, type the command

    python3 traffic.py [initialState] [heuristic]

Where the initialState argument is an int between 1 and 3 that determines which
inital puzzle (A, B, or C) that will be solved by the program.  The heuristic
argument is an int between 1 and 2 that determines which of our two heuristic
strategies will be used.  For example, the command

    python3 traffic.py 3 1

will solve puzzle C using heuristic one.  The command

    python3 traffic.py 1 2

will solved puzzle A using heuristic two.
