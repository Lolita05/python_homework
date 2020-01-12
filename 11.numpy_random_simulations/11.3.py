#monkey sort

#проверка отсортированности списка
def sorted_list(lst):
    #True - отсортирован False - не отсортирован
    sorted_list = True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            sorted_list = False
    return True if sorted_list else False

lst1 = [1, 2, 3]
lst2 = [2, 2, 1, 7]
sorted_list(lst1)
sorted_list(lst2)

#monkey sort
def monkey_sort(lst):
    i = 0
    while not sorted_list(lst):
        np.random.shuffle(lst)
        i += 1
    return i

#monkey sort визуализация
def monkey_sort_visualization():
    xx = range(2, 9)
    yy_M = []
    yy_SE = []
    num_of_iterations = 100
    for i in range(2, 9):
        print(i)
        speeds = []
        for _ in range(num_of_iterations):
            lst = np.random.standard_normal(i)
            speeds.append(monkey_sort(lst))
        M = sum(speeds)/len(speeds)
        SIGMA = np.sqrt(sum([(speed-M)**2 for speed in speeds])/len(speeds))
        SE = SIGMA/np.sqrt(len(speeds))
        yy_M.append(M)
        yy_SE.append(SE)
    plt.errorbar(xx, yy_M, yy_SE)
    plt.show()
