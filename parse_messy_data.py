from collections import defaultdict

def summarise_orders(lines:list[str]):
    orders = defaultdict(int)
    skipped = 0
    for line in lines:
        parts = line.split(":")
        if len(parts) != 2:
            skipped += 1
            continue

        item, price = parts[0].strip(), parts[1].strip()
        if not price.isdecimal():
            skipped += 1
            continue

        orders[item] += int(price)

    return (orders, skipped)

print(summarise_orders([]))
# ({}, 0)

print(summarise_orders(["pen: 100", "pen: 50", "bad line"]))
# ({"pen": 150}, 1)

print(summarise_orders(["a: 10", "b: xx", "c: 5"]))
# ({"a": 10, "c": 5}, 1)


"""
Initial mistakes
1. Split on whitespaces, would have missed coffee:1500, split on colon instead
2. strip(punctuation) removes negative sign, so -100 would been counted as 100
"""