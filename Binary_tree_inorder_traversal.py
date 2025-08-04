# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    # def add_child(self, data):
    #     if data == self.val:
    #         return
    #     if data < self.val:
    #         if self.left:
    #             self.left.add_child(data)
    #         else:
    #             self.left = TreeNode(data)
    #     else:
    #         if self.right:
    #             self.right.add_child(data)
    #         else:
    #             self.right = TreeNode(data)

class Solution:
    def inorderTraversal(self, root):
        res = []
        def inorder(root):
            if not root:
                return []
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res