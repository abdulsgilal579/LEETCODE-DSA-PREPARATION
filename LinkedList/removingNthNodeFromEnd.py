from LinkedList.linkedListImplementation import LinkedList

head = LinkedList.create([1, 2, 7, 4, 3, 9, 8, 5])

previousNode = None
fastPointer = head
slowPointer = head
nodeToRemoveFromEnd = 2
counter = 1

while counter <= nodeToRemoveFromEnd:
    nextNode = fastPointer.next
    fastPointer = nextNode
    counter += 1

if fastPointer is None:
    head = head.next
else:
    while fastPointer.next != None:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next
    slowPointer.next = slowPointer.next.next

print(head)