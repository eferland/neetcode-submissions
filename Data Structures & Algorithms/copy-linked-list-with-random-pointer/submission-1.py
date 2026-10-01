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
        newlist = []
        while head:
            temp = Node(head.val, None, head.random)
            newlist.append(temp)
            dict[head] = temp
            head = head.next
        newlist.append(None)
        dict[None] = None
        for i in range(len(newlist)-1):
            newlist[i].next = newlist[i+1] 
            newlist[i].random = dict[newlist[i].random]
        return newlist[0]


        