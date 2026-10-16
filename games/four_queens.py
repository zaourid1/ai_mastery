"""
Author: Zineb Aourid 
goal of this code is to build an agent to solve 4 queen puzzle for us

this is a goal-based agent, does not need ML or an LLM
"""

#board = [1, 3, 0, 2] this rep Q1 at col 1, Q2 at col 3,....
#Row 0 → Queen in column 1, Row 1 → Queen in column 3....

def is_safe(board, col):
    '''
     determines if its safe to place a queen in a col
    '''
    row = len(board)
    for previous_row in range(row):
        previous_col = board[previous_row]
        #checking if same col
        if col == previous_col:
            return False   
        #checking diagonal
        #|r1-r2| = |c1-c2| share a diagonal
        if abs(previous_row - row) == abs(previous_col - col):
            return False

    return True

def get_successors(board):
    '''
    suppose b = [1] queen @ pos (0,1), agent discovers only col 3 is safe for queen 2
    so succesor state = [1,3]
    '''
    successors = []

    for col in range(4):
        # 1. Check whether column is safe
        state = is_safe(board, col)
        
        #if state is safe so if state = True
        b = board.copy()
        if state:
            b.append(col)
            successors.append(b)

    return successors


def dfs():
    '''
    simple depth-first-search
    '''
    stack = [[]]

    while stack:
        current = stack.pop()

        # Check whether we've reached the goal, so all 4 queens placed
        if len(current) == 4:
            return current

        # Generate the next possible states
        successors = get_successors(current)

        # Add successors to the stack
        for state in successors:
            stack.append(state)

    return None
