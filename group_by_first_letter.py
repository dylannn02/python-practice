from collections import defaultdict

def group_by_first_letter(ls: list[str]):
    groups = defaultdict(list[str])
    for word in ls:
        letter = word[0].lower()
        groups[letter].append(word)

    return groups

print(group_by_first_letter(["Cat", "car", "dog"]))
# {'c': ['Cat', 'car'], 'd': ['dog']}
g = group_by_first_letter(["apple", "apricot", "banana", "blueberry"])
print(len(g)) # 2
g['z']
print(len(g)) # 3
g.get('q')
print(len(g)) # 3

# .get only ever reads, never mutates the dictionary

