from collections import defaultdict

def two_sum(ls:list, target:int):
    # use two pointer
    seen = {}
    for i, value in enumerate(ls):
        if target  - value in seen:
            return (seen[target-value], i)
        else:
            seen[value] = i
    return None

# two_sum([2, 7, 11, 15], 9) → (0, 1)
print(two_sum([2, 7, 11, 15], 9))

# two_sum([3, 2, 4], 6) → (1, 2)
print(two_sum([3, 2, 4], 6))

# two_sum([1, 2, 3], 7) → None
print(two_sum([1, 2, 3], 7))
