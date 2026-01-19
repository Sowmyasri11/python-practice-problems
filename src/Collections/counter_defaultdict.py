from collections import defaultdict

counter = defaultdict(int)
print(counter)

print(counter["dogs"])

print(counter)


counter["dogs"] += 1
counter["dogs"] += 1
counter["dogs"] += 1
counter["cats"] += 1
counter["cats"] += 1
print(counter)