from typing import Deque
class Node:
    def __init__(self , value = 0, left=None , right=None):
        self.value = value
        self.left = left
        self.right = right


class BTree:
    def __init__(self):
        self.root = None

def bfs(root):
    visited = []
    if root is None:
        return 0
    q = Deque()
    q.append(root)
    while q:
        curNode = q.popleft()
        visited.append(curNode.value)
        if curNode.left:
            q.append(curNode.left)
        if curNode.right:
            q.append(curNode.right)
    return visited

bt = BTree()
bt.root = Node(value=1)
bt.root.left = Node(value=2)
bt.root.right = Node(value=3)
bt.root.left.left = Node(value=4)
bt.root.left.right = Node(value=5)
bt.root.right.right = Node(value=6)

print(bfs(bt.root))
