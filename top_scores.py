def top_scorers(ls:list[tuple[str,int]]):
    results = []
    # sort ls using lambda by score, loop until score is less than 80, then break
    ls.sort(key=lambda s: s[1], reverse=True)
    for student in ls:
        if student[1] >= 80:
            results.append(student[0])
        else:
            break

    return results


print(top_scorers([("Maya", 92), ("Leo", 74), ("Priya", 88), ("Sam", 80), ("Nina", 65)])) 
#["Maya", "Priya", "Sam"]


print(top_scorers([("Alex", 50), ("Jo", 79)]))
# []

print(top_scorers([])) 
# []