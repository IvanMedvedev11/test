def min_(data):
    min_elem = data[0]
    for elem in data[1:]:
        if elem < min_elem:
            min_elem = elem
    return min_elem
def max_(data):
    max_elem = data[0]
    for elem in data[1:]:
        if elem > max_elem:
            max_elem = elem
    return max_elem
import random
try:
    n = int(input("Введите кол-во элементов в списке: "))
except ValueError:
    print("Прочитай внимательнее")
    quit()
list_ = [random.randint(-10**9, 10**9) for i in range(n)]
print(f'Минимум {min_(list_)}')
print(f'Максимум {max_(list_)}')
