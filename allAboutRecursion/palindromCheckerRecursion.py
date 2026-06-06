string = "racecar"


def isPalindromeRecursion(s):
    def helperRecursion(left, right):
        if left >= right:
            return True
        if string[left] != string[right]:
            return False
        return helperRecursion(left + 1, right - 1)

    return helperRecursion(left=0, right=len(s) - 1)


print(isPalindromeRecursion(string))
