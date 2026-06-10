from LinkedList.linkedListImplementation import LinkedList

head = LinkedList.create([7, 2, 7, 4, 3, 7, 8, 5])
val = 7

currentNode = head
previousNode = None

while currentNode:
    if currentNode.val == val:
        if previousNode is None:
            head = currentNode.next
        else:
            previousNode.next = previousNode.next.next
    else:
        previousNode = currentNode
    currentNode = currentNode.next


print(head)