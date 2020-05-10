num = list(map(int, list(input())))
print([sum(num[0:i]) for i in range(1, len(num) + 1)])
