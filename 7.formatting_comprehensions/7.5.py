# Имплементируйте бинарный поиск (принимает на вход элемент
# и отсортированный список, возвращает индекс с этим элементом)
list1 = [1, 3, 5, 'wow']


def binary_search(list, key, lo=0, hi=None):
    if hi is None:
        hi = len(list)
    while lo < hi:
        mid = (lo+hi)//2
        midval = list[mid]
        if midval < key:
            lo = mid+1
        elif midval > key:
            hi = mid
        else:
            return f"element {key} has index {mid}"
    return -1


print( binary_search(list1, 3))
