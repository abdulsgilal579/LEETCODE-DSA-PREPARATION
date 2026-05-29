class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        stack = []
        middle = len(values) // 2

        for nums in range(0, middle):
            stack.append(values[nums])

        if len(values) % 2 != 0:
            middle += 1

        while stack:
            if stack[-1] == values[middle]:
                stack.pop()
                middle += 1
            else:
                return False
        return True
