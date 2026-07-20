s = "ADOBECODEBANC"
t = "ABC"

def minimumWindowSubstring(s = None, t = t):
    if not s:
        return ""

    need = {}
    for i in t:
        if i in need:
            need[i] += 1
        else:
            need[i] = 1

    window = {}
    left = 0
    have = 0
    required = len(need)
    result = ""
    result_len = float("inf")

    for right in range(len(s)):
        c = s[right]
        window[c] = window.get(c, 0) + 1

        if c in need and window[c] == need[c]:
            have += 1
        
        while have == required:
            if (right - left + 1) < result_len:
                result = s[left:right+1]
                result_len = right - left + 1
            
            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1
            left +=1
        
    return result


print(minimumWindowSubstring(s = s, t = t))