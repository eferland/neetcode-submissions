# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        slow = slow.next
        prev = None
        while(slow is not None):
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        slow = prev

        # merge head, first half, and slow, rev second half
        res = head
        while head:
            temp = head.next
            head.next = slow
            if slow:
                slow = slow.next
            head = head.next
            if head:
                head.next = temp
                head = head.next
        head = res

