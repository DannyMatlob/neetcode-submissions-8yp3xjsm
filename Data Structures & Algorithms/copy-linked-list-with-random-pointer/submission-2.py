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
        if head is None:
            return None

        cur = head
        while cur is not None:
            next = cur.next
            cur.next = Node(cur.val)
            cur.next.next = next
            cur = next

        newHead = head.next

        cur = head
        while cur is not None:
            if cur.random is not None:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head
        while cur is not None:
            next = cur.next
            cur.next = next.next
            if next.next is not None:
                next.next = next.next.next
            cur = cur.next
        return newHead