from contextlib import nullcontext


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    previous = None
    current = head
    next = None

    while current != None:
        nextNode = current.next
        current.next = previous
        previous = current
        current = nextNode
    return previous


def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# Create: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original:")
print_list(head)

reversed_head = reverse_linked_list(head)

print("\nReversed:")
print_list(reversed_head)
