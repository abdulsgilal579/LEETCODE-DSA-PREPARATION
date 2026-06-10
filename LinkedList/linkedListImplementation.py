class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    @classmethod
    def create(cls, values):
        if not values:
            return None

        head = cls(values[0])
        current = head

        for val in values[1:]:
            current.next = cls(val)
            current = current.next

        return head

    def append(self, value):
        current = self

        while current.next:
            current = current.next

        current.next = LinkedList(value)

    def __str__(self):
        values = []
        current = self

        while current:
            values.append(str(current.val))
            current = current.next

        return " -> ".join(values) + " -> None"
