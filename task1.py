numbers_ = list(map(int, input("Введите список чисел: ").split()))
result = 0
for elem in numbers_:
    if elem >= 0:
        result += elem
print(result)
