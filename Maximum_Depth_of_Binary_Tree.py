# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Solution(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Solution(data)

    def in_order_traversal(self):
        elements = []
        
        # Visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit base node
        elements.append(self.data)

        # Visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
            
        return elements

    # Helps u to see the binary tree in the terminal
    def print_binary_search_tree(self, level=0):
        if self.data:
            if self.right:
                self.right.print_binary_search_tree(level + 1)

            print(' ' * 4 * level + '-> ' + str(self.data))

            if self.left:
                self.left.print_binary_search_tree(level + 1)

def build_tree(elements):
    root = Solution(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

def maxDepth(self, data):
    pass

if __name__ == '__main__':
    numbers = [3,9,20,15,7]
    tree_numbers = build_tree(numbers)
    print(tree_numbers.in_order_traversal())

    tree_numbers.print_binary_search_tree()