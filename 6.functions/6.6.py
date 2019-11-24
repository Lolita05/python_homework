#Мода
def mode(numbers):
    largestCount = 0
    modes = []
    for x in numbers:
        if x in modes:
            continue
        count = numbers.count(x)
        if count > largestCount:
            del modes[:]
            modes.append(x)
            largestCount = count
        elif count == largestCount:
            modes.append(x)
    return modes


s = [100, 3, 100, 2, 45, 45, 45, 3, 45, 3, 3, -2, 4]
print(mode(s))
