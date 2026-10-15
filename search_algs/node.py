"""
defining a node + a simple example tree to use for testing

for learning purposes: this was written by codex
"""


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root=None):
        self.root = root

    def display(self):
        if self.root is None:
            print("(empty tree)")
            return

        print(self.root.value)
        self._display_children(self.root, "")

    def _display_children(self, node, prefix):
        children = [("L", node.left), ("R", node.right)]
        children = [(side, child) for side, child in children if child is not None]

        for index, (side, child) in enumerate(children):
            is_last = index == len(children) - 1
            connector = "`-- " if is_last else "|-- "
            print(f"{prefix}{connector}{side}: {child.value}")
            child_prefix = prefix + ("    " if is_last else "|   ")
            self._display_children(child, child_prefix)


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

tree.display()
