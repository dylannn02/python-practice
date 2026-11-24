from collections import defaultdict

def group_anagrams(words:list[str]):
    anagrams = defaultdict(list)

    for word in words:
        sorted_word = "".join(sorted(word))
        anagrams[sorted_word].append(word)

    return list(anagrams.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]