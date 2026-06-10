from LinkedList.linkedListImplementation import LinkedList

head = LinkedList.create([1, 2, 3, 4, 5, 6, 7, 8, 10])

# Find middle
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

# Split list
secondHalf = slow.next
slow.next = None


# Reverse second half
def reverseLinkedList(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


secondHalf = reverseLinkedList(secondHalf)

# Merge two halves
first = head
second = secondHalf

while second:
    temp1 = first.next
    temp2 = second.next

    first.next = second
    second.next = temp1

    first = temp1
    second = temp2

print(head)


##LeetCode Submission

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         slow = head
#         fast = head
#
#         while fast and fast.next is not None:
#             slow = slow.next
#             fast = fast.next.next
#
#         secondHalf = slow.next
#         slow.next = None
#         firstHalf = head
#
#         previous = None
#         currentNode = secondHalf
#
#         while currentNode:
#             nextNode = currentNode.next
#             currentNode.next = previous
#             previous = currentNode
#             currentNode = nextNode
#
#         secondHalf = previous
#
#         while secondHalf:
#             temp1 = firstHalf.next
#             temp2 = secondHalf.next
#
#             firstHalf.next = secondHalf
#             secondHalf.next = temp1
#
#             firstHalf = temp1
#             secondHalf = temp2
#
#
#
#
#
