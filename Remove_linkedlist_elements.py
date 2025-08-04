# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        dummy = Node(0)
        dummy.next = head
        current = dummy
        
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
    
    def print(self, head=None):
        listz = []
        if head is None:
            print(listz)
            return
        while head:
            listz.append(head.val)
            head = head.next
        print(listz)

if __name__ == '__main__':
    linked_list = Node(1)
    linked_list.next = Node(2)
    linked_list.next.next = Node(6)
    linked_list.next.next.next = Node(3)
    linked_list.next.next.next.next = Node(4)
    linked_list.next.next.next.next.next = Node(5)
    test = Solution()
    new_head = test.removeElements(linked_list, 6)
    test.print(new_head)