"""
implementing breadth first search

class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
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

def bfs_search(tree,key):
    '''
    dont stop until all nodes searched or None
    '''
    #starting at root = 0
    curr = tree.root
    
    node_value = 0
    #seen = set()
    q = []
    while curr is not None:
        node_value += 1
        q.append(curr.value)
        if q[0] == key:
            return node_value, key
        
        curr = curr.left
        #node_value += 1

        if curr.value is not key:
            #node_value += 1
            curr = curr.parent.right


        
       

    return None
    

print(bfs_search(tree,key))
