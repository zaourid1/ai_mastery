"""
implementing breadth first search

class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

Notes: took me some time
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
    node_value = 0
    q = []
    if tree.root is None:
        pass
    else:
        q.append(tree.root)
    
    while q:
        node_value += 1
      
        n = q[0]
        #print("node: ", n.value)
        
        if n.value == key:
            return node_value, key
        
        else:
            q.pop(0)
            if n.left is not None:
                q.append(n.left)

            if n.right is not None:
                q.append(n.right)

        #curr = q[0]
        
    return None
    

print(bfs_search(tree,key))

print(bfs_search(tree,key="C"))

print(bfs_search(tree,key="Z"))
