"""
trying to code 4 queens problem using python.

problem: given 4X4 empty chessboard, place 4 queens so not no two queens
attack each other.

valid solution:
[(0,1), (1,3), (2,0), (3,2)]

__|Q |__|__
__|__|__|Q
Q |__|__|__
__|__|Q |__

"""

def solveFourQueens():
    # Store the column chosen for each row.
    board = []
    solutions = []

    def is_safe(row, col):
        # TODO: Check whether this position conflicts with a placed queen.
        #check whether this pos conflicts w a placed queen.
        
        
        pass

    def backtrack(row):
        # TODO: If every row has a queen, save the current board.
        # TODO: Otherwise, try each column in this row.
        # TODO: For each safe position, place a queen, recurse, then undo it.
        pass

    # TODO: Start the search at the first row.
    # TODO: Return the solutions found.
    pass