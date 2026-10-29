# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0 
        count = head; 
        while(count != None):
            counter += 1
            count = count.next
        
        length = counter - (n+1)
        remover = head
        returner = remover
        if(counter == n):
            return(returner.next)

        while(length > 0):
            remover = remover.next
            length -= 1
        remover.next = remover.next.next
        return(returner)


        
       
