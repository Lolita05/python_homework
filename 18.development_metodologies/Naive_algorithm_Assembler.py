#Exact matching

def naive(p, t):
    occurences =[]
    for i in range(len(t) - len(p) + 1):
    match = True
        for j in range(len(p)):
            if t[i + j] != p[j]:
                match = false
                break
        if match:
            occurences.append(i)
    return occurences
