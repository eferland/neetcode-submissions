# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        curr1 = list1
        curr2 = list2
        if(list1.val <= list2.val):
            outlist = list1
            curr1 = curr1.next
        else:
            outlist = list2
            curr2 = curr2.next
        curr = outlist
        while (curr1 is not None or curr2 is not None):
            if(curr2 is None):
                curr.next = curr1
                curr1 = curr1.next
            elif(curr1 is None):
                curr.next = curr2
                curr2 = curr2.next
            elif(curr1.val<=curr2.val):
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        return outlist

        
