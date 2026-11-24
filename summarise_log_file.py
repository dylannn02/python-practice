from collections import Counter

def count_actions(path:str):
    counts = Counter()
    with open(path) as file:
        text = file.read()

    lines = text.split("\n")
    for line in lines:
        parts = line.split(":")
        if len(parts) != 2:
            continue
        name, activity = parts[0].strip(), parts[1].strip()
        if not name or not activity:
            continue
        
        counts[name] += 1

    return counts

assert count_actions("activity.log") == {"maya": 3, "leo": 2, "priya": 1}
print(count_actions("activity.log"))
# {"maya": 3, "leo": 2, "priya": 1}

assert count_actions("empty.log") == {}
print(count_actions("empty.log"))
# {}