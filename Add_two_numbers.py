# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
          

test = ListNode(2)
test.next = ListNode(4)
test.next.next = ListNode(3)

test2 = ListNode(5)
test2.next = ListNode(6)
test2.next.next = ListNode(4)

jet = Solution()
jet.addTwoNumbers(test, test2)