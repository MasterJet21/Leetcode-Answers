# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def addchild(self, data):
        if data == self.val:
            return
        if data < self.val:
            if self.left:
                self.left.addchild(data)
            else:
                self.left = TreeNode(data)
        else:
            if self.right:
                self.right.addchild(data)
            else:
                self.right = TreeNode(data)

class Solution():
    def invert(self, root):
        inv = []
        stack = []
        while root or stack:
            while root:
                root.right, root.left = root.left, root.right
                stack.append(root)
                root = root.right

        root = stack.pop()
        inv.append(root)
        root = root.left

        return inv

# Input[4,2,7,1,3,6,9]
# Output[4,7,2,9,6,3,1]

# | Method Type         | Bound To       | Accesses                    | Keyword Used      | Common Use                                       |
# | ------------------- | -------------- | --------------------------- | ----------------- | ------------------------------------------------ |
# | **Instance Method** | Instance       | `self`, instance attributes | `self`            | Regular behavior tied to object state            |
# | **Class Method**    | Class          | `cls`, class attributes     | `@classmethod`    | Factory methods, class-level operations          |
# | **Static Method**   | None (unbound) | No instance/class access    | `@staticmethod`   | Utility/helper logic unrelated to class state    |
# | **Magic Methods**   | Instance       | `self`, invoked by Python   | `__name__` format | Operator overloading, string representation, etc |
    