"""
tesing our Four_queen.py functions
Author: Zineb Aourid
"""
from four_queens import is_safe, get_successors, dfs

b = [1,3]
print(is_safe(b, col=1))
print(is_safe(b, col=0))


print(get_successors([]))
# Expected: [[0], [1], [2], [3]]

print(get_successors([1]))
# Expected: [[1, 3]]

print(get_successors([0]))
# Expected: [[0, 2], [0, 3]]

print(dfs())