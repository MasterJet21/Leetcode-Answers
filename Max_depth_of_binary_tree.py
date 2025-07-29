# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if root is None:
            return -1
    
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return max(left_height, right_height) + 1
    

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def preorder(root):
#     """Preorder Traversal: Root → Left → Right"""
#     if root:
#         print(root.value, end=' ')
#         preorder(root.left)
#         preorder(root.right)

# def inorderTraversal(root):
#     if root:
#         inorderTraversal(root.left)
#         print(root.val, end=' ')
#         inorderTraversal(root.right)

# def postorder(root):
#     """Postorder Traversal: Left → Right → Root"""
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.value, end=' ')

# # Example Usage
# if __name__ == "__main__":
#     # Constructing the binary tree
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)

#     print("Preorder Traversal:")
#     preorder(root)  # Output: 1 2 4 5 3
#     print("\nInorder Traversal:")
#     inorder(root)   # Output: 4 2 5 1 3
#     print("\nPostorder Traversal:")
#     postorder(root) # Output: 4 5 2 3 1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode()
root.left.right = TreeNode()
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

inorder(root)