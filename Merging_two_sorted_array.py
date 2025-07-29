# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def merge_lists(head1, head2):
        temp = N
        temp.next = N  # which means N.next = N
        N = N.next 

        if head1 is None:
            return head2
        if head2 is None:
            return head1

    # create dummy node to avoid additional checks in loop
        s = t = Node()
        while not (head1 is None or head2 is None):
            if head1.value < head2.value:
                # remember current low-node
                c = head1
                # follow ->next
                head1 = head1.next
            else:
                # remember current low-node
                c = head2
                # follow ->next
                head2 = head2.next

            # only mutate the node AFTER we have followed ->next
            t.next = c 
            # and make sure we also advance the temp
            t = t.next

        t.next = head1 or head2

        # return tail of dummy node
        return s.next

if __name__ == '__main__':
    solution = Node()
    