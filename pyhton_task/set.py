
set1 = {1, 2, 3, 2, 3, 1, "one", 'one', "One"}
set2 = {1, 2, 3, 2, 1, 3}

empty_set = set()
print(set1)

print(set1.intersection(set2))
print(set1 & set2)
print(set1 | set2)
print(set1.union(set2))