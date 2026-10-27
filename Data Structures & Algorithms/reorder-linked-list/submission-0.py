# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return
        back = ListNode()
        temp = None
        s, f = head, head
        first = head
        while f.next != None and f.next.next != None:
            f = f.next.next
            s = s.next
        s2 = s.next
        s.next = None
        s = s2
        while s != None:
            temp2 = s.next
            s.next = temp
            temp = s
            s = temp2
        temper = back
        while first != None:
            temper.next = first
            first = first.next
            temper = temper.next
            if temp != None:
                temper.next = temp
                temp = temp.next
                temper = temper.next
        temper.next = None