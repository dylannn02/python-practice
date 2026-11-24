

def flatten(nest:list):
    # if next element is a list, we go into the list, and return the first element of that list
    # else if its an int, we move to the next element
    for element in nest:
        if type(element) == list:
            yield from flatten(element)
        else:
            yield element
    return

print(list(flatten([1, [2, [3, 4], 5], [], [6]])))
# [1, 2, 3, 4, 5, 6]

print(list(flatten([])))
# []

print(list(flatten([[], [[], []]])))
# []

assert list(flatten([1, 2, 3])) == [1, 2, 3]
assert list(flatten([[1], [2], [3]])) == [1, 2, 3]
assert list(flatten([[[1]]])) == [1]
assert list(flatten([1, [], 2, [[], 3]])) == [1, 2, 3]
assert list(flatten([[[[5]]]])) == [5]
assert list(flatten([[], [], []])) == []
assert list(flatten([7])) == [7]

"""
yield from flatten(item)

is the same as

for value in flatten(item):
    yield value
"""