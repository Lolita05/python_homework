# Имплементируйте линейный поиск (принимает на вход элемент и список, возвращает индекс с этим элементом)
list1 = [1, 3, 5, 'wow']


def line_search(list, key):
    for i in range (len(list)):
        if list[i] == key:
            return f"element {key} has index {i}"

print(line_search(list1, 3))
