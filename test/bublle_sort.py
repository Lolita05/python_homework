#Сортировка пузырьком
list_for_sort = [0, 5, 8, 4, 9, 3]
list_for_sort2 = [0, 0, 1, 1, 34]
list_for_sort3 = [56, 0, 78, 1, 34]


def bubble_sort(list_for_sort):
    N = len(list_for_sort)
    for i in range(N-1):
        for j in range(N-1, i, -1):
            if list_for_sort[j] < list_for_sort[j-1]:
                list_for_sort[j], list_for_sort[j - 1] = list_for_sort[j - 1], list_for_sort[j]
    return list_for_sort

print(bubble_sort(list_for_sort))
print(bubble_sort(list_for_sort2))
print(bubble_sort(list_for_sort3))
