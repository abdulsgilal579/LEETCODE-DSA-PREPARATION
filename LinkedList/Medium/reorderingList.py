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