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
            if not l1 and not l2:
                curr.next = ListNode(carry, None)
                return dummy.next
            elif not l1:
                value = (l2.val+carry)%10
                carry = 1 if l2.val==9 else 0
                l2 = l2.next
            elif not l2:
                value = (l1.val+carry)%10
                carry = 1 if l1.val==9 else 0
                l1 = l1.next
            else:
                add = l1.val+l2.val+carry
                value = add%10
                carry = add//10
                l1 = l1.next
                l2 = l2.next
            curr.next = ListNode(value, None)
            curr = curr.next
        return dummy.next
    



        