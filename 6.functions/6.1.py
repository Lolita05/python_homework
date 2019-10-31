#flat list
def flatten(li):
    return sum(([x] if not isinstance(x, list) else flatten(x)
                for x in li), [])
l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
print(flatten(l))