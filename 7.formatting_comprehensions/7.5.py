# Имплементируйте бинарный поиск (принимает на вход элемент
# и отсортированный список, возвращает индекс с этим элементом)
list1 = [1, 3, 5, 'wow']

def binary_search(list, key):
    left = -1
    right = len(list)
    while right > left + 1:
        middle = (left + right) // 2
        if list1[middle] >= key:
            right = middle
        else:
            left = middle
    return f"element {key} has index {right}"

print( binary_search(list1, 3))
