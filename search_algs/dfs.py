"""
dsf - depth first search

notes: LiFo Stack
"""
from node import Node, Tree

# Example tree:
#          A
#        /   \
#       B     C
#      / \   / \
#     D   E F   G
root = Node("A")
root.left = Node("B", parent=root)
root.right = Node("C", parent=root)
root.left.left = Node("D", parent=root.left)
root.left.right = Node("E", parent=root.left)
root.right.left = Node("F", parent=root.right)
root.right.right = Node("G", parent=root.right)

tree = Tree(root)
key = 'G'

def dfs_print(tree):
    '''
    just printing tree using dfs, no search for now
    '''
    stack = []
    traversal_values = []
    if tree.root is None:
        pass
    else:
        stack.append(tree.root)    
   
    while stack:
        curr = stack.pop()
        traversal_values.append(curr.value)
        if curr.right:
            stack.append(curr.right)
    
        if curr.left:
            stack.append(curr.left)

    return traversal_values

print(dfs_print(tree))