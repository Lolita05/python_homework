#Разверните строку всеми известными вам способами
#1
s = 'agatacaca' [::-1]
print = s

#2
s1 = 'agatacaca'
s2 = ''
i = len(s1)-1
while (i>=0):
    s2 = s2 +s1[i]
    i = i-1
print(s2)

#3
def r(s):
    if len(s) == 0:
        return s
    else:
        return r(s[1:]) + s[0]
s1 = 'agatacaca'
s2 = r(s1)
print(s2)

#4
s = 'agatacaca'
list = list(s)
list.reverse()
s1 = ''.join(list)
print(s1)

#5
print(''.join(reversed('agatacaca')))
