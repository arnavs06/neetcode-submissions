# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                node.next = list2
                list2 = list2.next
            else:
                node.next = list1
                list1 = list1.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
        '''

        so for linked lists its:

        list1.val
        list2.val

        sorted, so compare list1.val vs list2.val, which ever one is less becomes the new curr, and 

        1 -> 2 -> 4

        1 -> 3 -> 5

        1 -> 1 -> 2 -> 3 -> 4 -> 5


        curr = list1.val
        next_node = list1.next
        if list1.val >= list2.val:
            list1.next == list2.val
        else:
            list1.next == list2.val

            curr = list1.next

        
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                node.next = list2.val
                list2 == list2.next
            else
                list1 = list1.val
            node = node.next

            node.next = list1 or list2
            return dummy

        '''

            
        

        
    

        