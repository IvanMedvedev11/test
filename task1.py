try:
    numbers_ = list(map(int, input("Введите список чисел: ").split()))
except ValueError:
    print("Ты И Д И О Т")
    quit()
result = 0
for elem in numbers_:
    if elem >= 0:
        result += elem
print(result)
