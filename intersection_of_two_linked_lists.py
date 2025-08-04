# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        d = {}
        if get_length(headA) < get_length(headB):
            while headA:
                if headA not in d:
                    d.update({headA: 1})
                    headA = headA.next
                else:
                    return headA
            while headB:
                if headB not in d:
                    d.update({headB: 1})
                    headB = headB.next
                else:
                    return headB
                
        else:
            while headB:
                if headB not in d:
                    d.update({headB: 1})
                    headB = headB.next
                else:
                    return headB
            while headA:
                if headA not in d:
                    d.update({headA: 1})
                    headA = headA.next
                else:
                    return headA

        return None

def get_length(head):
    leng = 0
    while head:
        leng += 1
        head = head.next
    return leng