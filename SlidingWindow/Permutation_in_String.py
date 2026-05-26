# 567. Permutation in String

s1 = "ab"
s2 = "eidbaooo"

def permutationInString(string1, string2):
    if len(string1) > len(string2):
        return False
    s1HashMap = {}
    windowHashMap = {}
    left = 0

    for character in string1:
        if character not in s1HashMap:
            s1HashMap[character] = s1HashMap.get(character, 0) + 1
        else:
            s1HashMap[character] += 1
        
    for right in range(len(string2)):
        windowHashMap[string2[right]] = windowHashMap.get(string2[right], 0) + 1
        windowSize = right - left + 1

        if windowSize > len(string1):
            windowHashMap[string2[left]] -= 1
            if windowHashMap[string2[left]] == 0:
                del windowHashMap[string2[left]]
            left += 1

        if windowHashMap == s1HashMap:
            return True
    return False



    
    
