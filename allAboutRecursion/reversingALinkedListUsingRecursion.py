# 1 -> 2 -> 3 -> 4 -> 5


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
