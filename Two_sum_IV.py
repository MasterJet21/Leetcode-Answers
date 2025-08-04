# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, data):
        if data < self.val:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)

class Solution:
    def findTarget(self, root, k):
        seen = set()
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
                    
            root = stack.pop()
            
            if (k - root.val) not in seen:
                seen.add(root.val)
            else:
                return True

            root = root.right
        
        return False
        

tree = TreeNode(5)
tree.insert(3)
tree.insert(6)
tree.insert(2)
tree.insert(4)
tree.insert(7)
print(tree)