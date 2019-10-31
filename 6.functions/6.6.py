#Мода
def mode(arr) :
    f = {}
    for a in arr : f[a] = f.get(a,0)+1
    m = max(f.values())
    t = [(x,f[x]) for x in f if f[x]==m]
    return m > 1 t[0][0] else None
s = [100, 3, 100, 2, 45, 45, 45, 3, 45, 3, 3, -2, 4]
print(mode(s))
