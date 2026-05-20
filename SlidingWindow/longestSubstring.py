s = "abcabcbb"


def longestSubString(string):
    left = 0
    right = 0
    maximumString = 0
    stringSet = set()

    for right in range(len(string)):
        while string[right] in stringSet:
            stringSet.remove(string[left])
            left += 1
        stringSet.add(string[right])
        maximumString = max(maximumString, right - left + 1)
    return maximumString
        
print(longestSubString(string=s))