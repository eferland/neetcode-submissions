# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = curr = ListNode(0, None)
        while l1 or l2 or carry:
            left = 0 if not l1 else l1.val
            right = 0 if not l2 else l2.val
            value = (left+right+carry)%10
            curr.next = ListNode(value, None)
            carry = 1 if left+right+carry>=10 else 0
            curr = curr.next
            l1 = l1 if not l1 else l1.next
            l2 = l2 if not l2 else l2.next
        return dummy.next
    



        