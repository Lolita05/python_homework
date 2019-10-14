# Вывод таблиц истинности

# not
def NOT(a):
    if(a == 0):
        return 1
    elif(a == 1):
        return 0
def main():
    print("| a | not a |")
    print("-------------")
    for a in [0, 1]:
            print('|', a, '|', NOT(a), '|')
main()

# or
def OR(a, b):
    if a == 1:
        return 1
    elif b == 1:
        return 1
    else:
        return 0
def main():
    print("| a | b | a or b |")
    print("------------------")
    for a in [0, 1]:
        for b in [0, 1]:
            print('|', a, '|' , b, '|', OR(a, b), '|')
main()

# xor
def XOR(a, b):
    if a != b:
        return 1
    else:
        return 0
def main():
    print("| a | b | a xor b |")
    print("------------------")
    for a in [0, 1]:
        for b in [0, 1]:
            print('|', a, '|' , b, '|', XOR(a, b), '|')
main()

# nor
def NOR(a, b):
    if(a == 0) and (b == 0):
        return 1
    elif(a == 0) and (b == 1):
        return 0
    elif(a == 1) and (b == 0):
        return 0
    elif(a == 1) and (b == 1):
        return 0
def main():
    print("| a | b | a nor b |")
    print("------------------")
    for a in [0, 1]:
        for b in [0, 1]:
            print('|', a, '|' , b, '|', NOR(a, b), '|')
main()

# and
def AND(a, b):

	if a == 1 and b == 1:
		return 1
	else:
		return 0
def main():
    print("| a | b | a and b |")
    print("------------------")
    for a in [0, 1]:
        for b in [0, 1]:
            print('|', a, '|' , b, '|', AND(a, b), '|')
main()

# nand
def NAND(a, b):
    if a == 1 and b == 1:
        return 0
    else:
        return 1
def main():
    print("| a | b | a nand b |")
    print("------------------")
    for a in [0, 1]:
        for b in [0, 1]:
            print('|', a, '|' , b, '|', NAND(a, b), '|')
main()
