# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1 = list1
        l2 = list2
        a = ListNode()
        head = a
        while(l1 != None and l2 != None):
            temp = None 
            if(l1.val < l2.val):
                temp = l1
                l1 = l1.next 
                a.next = temp
            else:
                temp = l2
                l2 = l2.next 
                a.next = temp
            a = a.next
        a.next = l1 or l2
        return(head.next)
        