# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        naheadnode = head
        for _ in range(n):
            naheadnode = naheadnode.next
        if not naheadnode:
            return head.next
        
        naheadnode = naheadnode.next
        start = head
        while naheadnode:
            start = start.next
            naheadnode = naheadnode.next
        start.next = start.next.next
        return head