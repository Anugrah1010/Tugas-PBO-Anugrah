def increment(x):
    return x + 3

numbers = [1, 2, 3, 4, 5]

result = map(increment, numbers)
print(list(result))  # [4, 5, 6, 7, 8]
