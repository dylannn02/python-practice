# Write a generator function called pages that splits a list into pages of a given size, yielding one page at a time.

def pages(items, size):
    for i in range(0, len(items), size):
        yield items[i:i+size]

print(type(pages([1,2],1))) # <class 'generator'>

print(list(pages([1, 2, 3, 4, 5], 2)))
# [[1, 2], [3, 4], [5]]

book = pages([1,2,3,4,5,6,7], 3) # generator object
print(next(book)) # we can call next() on a generator object
# [1, 2, 3]

# we can iterate through a generator object
for page in book:
    print(page)

# [4, 5, 6]
# [7]

# notice we dont have [1, 2, 3] again because we already called next() on book and consumed the first item
# generators remembers where it paused