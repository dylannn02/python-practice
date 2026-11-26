def is_balanced(s:str):
    bracket_lookup = {")" : "(", "]": "[", "}": "{"}
    stack = []

    for bracket in s:
        if bracket not in bracket_lookup:
            stack.append(bracket)

        elif stack and bracket_lookup[bracket] == stack[-1]:
            stack.pop()
        else:
            return False

    if not stack:
        return True
    else:
        return False

assert is_balanced("([])") is True
assert is_balanced("([)]") is False
assert is_balanced("((()))") is True
assert is_balanced("([") is False
assert is_balanced("") is True
assert is_balanced("{[()]}") is True
assert is_balanced("}{") is False
