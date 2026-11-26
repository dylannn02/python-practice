from collections import defaultdict
def longest_substring(s:str):
    seen = defaultdict(int) # store each char's index
    left, right = 0, 0
    longest = 0
    curr = 0
    while right < len(s):
        if s[right] in seen and seen[s[right]] >= left:
            longest = max(longest, curr)
            left = seen[s[right]] + 1
            seen[s[right]] = right
            curr = right - left + 1
            right += 1
        else:
            seen[s[right]] = right
            curr += 1
            right += 1

    return max(longest,curr)

assert longest_substring("abcabcbb") == 3
assert longest_substring("bbbbb") == 1
assert longest_substring("pwwkew") == 3
assert longest_substring("") == 0
assert longest_substring("abcdef") == 6
assert longest_substring("dvdf") == 3

"""
weak points, didnt know to bring left to just 1 index after the seen char, instead i set left to right
new curr computation should be whatever the window is after moving left, which is right - left + 1
"""