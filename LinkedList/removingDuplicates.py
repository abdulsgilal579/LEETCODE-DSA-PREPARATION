from LinkedList.linkedListImplementation import LinkedList

head = LinkedList.create([1, 2, 3, 3, 3, 4, 4, 5])

currentNode = head

while currentNode and currentNode.next:
    nextNode = currentNode.next
    if nextNode.val == currentNode.val:
        currentNode.next = nextNode.next
    else:
        currentNode = nextNode

print(head)
