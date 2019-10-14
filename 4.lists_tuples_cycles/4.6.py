elements = [1, 2, ('fruit', 5)]
print (elements[::-1]) #1

elements = [1, 2, ('fruit', 5)]
print (elements[::~0]) #2

elements = [1, 2, ('fruit', 5)]
elements.reverse()
print (elements) #3

elements = [1, 2, ('fruit', 5)]
a = list(reversed(elements))
print (a) #4

elements = [1, 2, ('fruit', 5)]
for i in range(int(len(elements) / 2)):
    elements[i], elements[len(elements)-1-i] = elements[len(elements)-1-i], elements[i]
print(elements) #5

elements = [1, 2, ('fruit', 5)]
elements = [i for in range(len(elements) -1, -1, -1)]
print(elements) #6

elements = [1, 2, ('fruit', 5)]
f = lambda elements: (f(elements[1:]) + elements[:1] if elements else [])
print(f(elements)) #7
