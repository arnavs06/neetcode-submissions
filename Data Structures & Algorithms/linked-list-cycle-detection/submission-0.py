# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        use 2 pointers, slow and fast, with fast moving twice as fast as slow


        so then you can check the existence of a cycle by if the fast catches up to the slow

       given LL 1 -> 2 -> 3 -> 4:

       if index = 1, then head.next = index 1 in the LL

       so it becomes 1 -> 2 -> 3 -> 4 -> 2 -> 3 -> 4 forever


        1 -> 2 -> 3 -> 4 -> 2 -> 3 -> 4 -> 2 -> 3 -> 4 -> 2 -> 3 -> 4

                        s
                                      f

        so move each slow pointer once, and each fast pointer twice, and if the slow == fast at all, then there is a cycle else not

        slow, fast = head, head #starting the pointers at the same position

        while fast and fast.next:
            slow = slow.next #move each slow pointer once
            fast == fast.next.next #move each fast pointer twice
            if slow == fast:
                return True # this means there is a cycle, because the gap closes by 1 each cycle 
            False 

        '''
        slow, fast = head, head #starting the pointers at the same position

        while fast and fast.next:
            slow = slow.next #move each slow pointer once
            fast = fast.next.next #move each fast pointer twice
            if slow == fast:
                return True # this means there is a cycle, because the gap closes by 1 each cycle 
        return False 