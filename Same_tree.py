# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root):
    if not root:
        return []
    
    q = deque([root])
    ls = []

    while q:
        node = q.popleft()
    
        if node:
            ls.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            ls.append(None)
    
    return ls

class Solution:
    def isSameTree(self, p, q):
        p_new = bfs(p)
        q_new = bfs(q)
        if p_new == q_new:
            return True
        return False


# tree = TreeNode(1)
# tree.next = TreeNode(2)
# tree.next.next = TreeNode(3)


# visited = [] # List for visited nodes.
# queue = []     #Initialize a queue

# def bfs(visited, node1, node): #function for BFS
#   visited.append(node)
#   queue.append(node)

#   while queue:          # Creating loop to visit each node
#     m = queue.pop(0) 
#     print (m, end = " ")

#     for neighbour in node1:
#       if neighbour not in visited:
#         visited.append(neighbour)
#         queue.append(neighbour)

# # Driver Code
# print("Following is the Breadth-First Search")
# bfs(visited, graph, '5')    # function calling