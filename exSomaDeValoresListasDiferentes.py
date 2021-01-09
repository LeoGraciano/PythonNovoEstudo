list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]

total = [sum(t) for t in zip(list_a, list_b)]

print(total)
