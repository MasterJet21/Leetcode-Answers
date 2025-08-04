# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        def insert(self, val):
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            else:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)

class Solution:
    def preorder_traversal(self, val):
        res = []
        def preorder(root):
            if not root:
                return []
            preorder(root.left)
            res.append(root.val)
            preorder(root.right)

        preorder(val)
        return res

    def sortedArrayToBST(self, nums):
        pass