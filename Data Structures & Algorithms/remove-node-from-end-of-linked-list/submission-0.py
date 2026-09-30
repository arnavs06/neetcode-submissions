# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        3 steps:

        1. create dummy node that points to the head, and 2 slow and fast nodes at the same position
        2. move the fast node by n steps with a for loop
        3. move both slow and fast until fast.next points to null, and then fast and slow will be n nodes apart from eachother, so then slow will be the nth node of the list, which then you just remove it by skipping it by making the previous node to the nth one point to the n+1 node


        1 -> 2 -> 3 -> 4


        
        '''

        dummy = ListNode(0,head)
        slow = fast = dummy

        for i in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next