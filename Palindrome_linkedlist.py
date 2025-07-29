# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Use Slow and Fast pointer technique, 2 pointers at the first node, 1st pointer increment/move up by one, 
# the other pointer increment by 2. When the fast pointer reach null, first pointer is
# in the middle/at the first of the two middle nodes.
class Solution:
    def isPalindrome(self, head):
        node = None
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        while slow:
            temp = slow.next # Disconnects the current node to the next node
            slow.next = node # Connects current node to the empty/None node
            node = slow # Pointer of the empty node go to current node
            slow = temp # Current node pointer go to the next node

        first = head
        second = node
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True