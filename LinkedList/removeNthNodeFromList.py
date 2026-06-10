from http.cookiejar import cut_port_re

from LinkedList.linkedListImplementation import LinkedList

head = LinkedList.create([1, 2, 7, 4, 3, 9, 8, 5])

previousNode = None
currentNode = head
node = 1
counter = 1

if node==1:
    nextNode = currentNode.next
    head = nextNode

else:
    while counter < node:
        previousNode = currentNode
        nextNode = currentNode.next
        currentNode = nextNode
        counter += 1

    nextNode = currentNode.next
    previousNode.next = nextNode

print(head)


