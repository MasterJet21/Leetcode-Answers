# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print(self):
        current = self
        while current:
            print(current.val, end="-->")
            current = current.next
        print("None")
class Solution():
    def deleteDuplicates(self, head):
        ls = []
        current = head
        while current and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

node = ListNode(1)
node.next = ListNode(1)
node.next.next = ListNode(2)
node.next.next.next = ListNode(2)
node.next.next.next.next = ListNode(3)

node.print()
node.deleteDuplicates()
node.print()