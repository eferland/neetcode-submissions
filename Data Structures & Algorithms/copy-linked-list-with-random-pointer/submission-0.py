"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dict = {}
        # indexdict = {}
        newlist = []
        count = 0
        while head:
            newlist.append(Node(head.val, None, head.random))
            dict[head] = count
            # indexdict[head] = count
            count+=1
            head = head.next
        newlist.append(None)
        dict[None] = count
        for i in range(len(newlist)-1):
            newlist[i].next = newlist[i+1] 
            newlist[i].random = newlist[dict[newlist[i].random]]
        return newlist[0]


        