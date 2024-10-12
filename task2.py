def binary_search(data, elem):
    low = 0
    high = len(data) - 1
    while low <= high:
        middle = (low + high) // 2
        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1
    return -1
import random
a = random.randint(0, 1000)
b = random.randint(1001, 2000)
list_ = [i for i in range(a, b+1)]
try:
    number = int(input("Введите число: "))
except ValueError:
    print("ЧИТАТЬ научись")
    quit()
if binary_search(list_, number) != -1:
    print("Элемент принадлежит промежутку")
else:
    print("Элемент не принадлежит промежутку")
