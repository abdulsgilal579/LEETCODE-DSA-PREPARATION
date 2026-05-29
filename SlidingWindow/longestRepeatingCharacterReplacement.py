string = "AABABBA"
k = 1


def longestRepeatingCharacterReplacement(string, k):
    hashMap = {}
    maxFrequency = 0
    maxLength = 0
    left = 0
    right = 0

    for right in range(len(string)):
        if string[right] not in hashMap:
            hashMap[string[right]] = hashMap.get(string[right], 0) + 1
        else:
            hashMap[string[right]] += 1

        maxFrequency = max(maxFrequency, hashMap[string[right]])

        windowLength = right - left + 1
        replacementNeeded = windowLength - maxFrequency

        if replacementNeeded > k:
            hashMap[string[left]] -= 1
            left += 1

        maxLength = max(maxLength, right - left + 1)
    return maxLength


print(longestRepeatingCharacterReplacement(string=string, k=k))
