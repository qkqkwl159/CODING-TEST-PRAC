
from typing import Deque


def bfs(root) 
    visited =[]
    if root is None:
        return
    q = Deque()
    q.append(root)
    while q:
        curNode = q.popleft()
        visited.append(curNode)
        if curNode.left:
            q.append(curNode.left)
        if curNode.right:
            q.append(curNode.right)
    return visited
