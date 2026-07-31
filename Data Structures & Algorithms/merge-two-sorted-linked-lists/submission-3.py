# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
        prev = None means there is no previous value in the linked list
        
        and curr = head means you're starting at the beginning of the 
        linked list and the first value is the curent one which is the head 
        (head -> tail for LL)

        now the while loop is there to check every element in the linked list

        next_node = curr.next literally just traverses to the next node in the LL

        curr.next = prev and prev = curr is the part that reverses the linked list,



        '''
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


    

