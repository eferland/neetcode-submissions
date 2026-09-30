# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slowhead = head
        fasthead = head.next
        while(fasthead is not None):
            if fasthead == slowhead:
                return True
            elif(fasthead.next is None):
                return False
            else:
                slowhead = slowhead.next
                fasthead = fasthead.next.next
        return False