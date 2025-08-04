# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head):
        dict = {}
        index = 0
        while head:
            if head in dict.values():
                return True
            dict.update({index: head})
            index += 1
            head = head.next
        return False
    
    def print(self):
        if self.head is None:
            print("Linkedlist is empty.")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next

tree = ListNode(3)
tree.next = ListNode(2)
tree.next.next = ListNode(0)
tree.next.next.next = ListNode(-4)

iterator = tree
while iterator is not None:
    print(iterator.val)
    iterator = iterator.next
