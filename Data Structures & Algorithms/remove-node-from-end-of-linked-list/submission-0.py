# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        start = head
        while head:
            head = head.next
            length+=1
        head = start
        if(length-n==0):
            return head.next
        for i in range(length-n-1):
            head = head.next
        head.next = head.next.next
        return start
        