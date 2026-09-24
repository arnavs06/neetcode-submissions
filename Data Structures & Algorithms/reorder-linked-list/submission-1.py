# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        3 steps:

        1) split linked list
        2) reverse 2nd half of linked list
        3) add both together in order of first, second til end
'''

        #step 1:

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #step 2:

        second = slow.next
        slow.next = None 

        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        
        #step 3:
        first, second = head, prev


        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2