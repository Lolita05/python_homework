# Вывод таблиц истинности

# not
def NOT(a):
    if(a == False):
        return True
    elif(a == True):
        return False
def main():
    print("| a | not a |")
    print("-------------")
    for a in [False, True]:
            print('|', a, '|', NOT(a), '|')
main()

# or
def OR(a, b):
    if a is True:
        return True
    elif b is True:
        return True
    else:
        return False
def main():
    print("| a | b | a or b |")
    print("------------------")
    for a in [False, True]:
        for b in [False, True]:
            print('|', a, '|' , b, '|', OR(a, b), '|')
main()

# xor
def XOR(a, b):
    if a != b:
        return True
    else:
        return False
def main():
    print("| a | b | a xor b |")
    print("------------------")
    for a in [False, True]:
        for b in [False, True]:
            print('|', a, '|' , b, '|', XOR(a, b), '|')
main()

# nor
def NOR(a, b):
    if(a == False) and (b == False):
        return True
    elif(a == False) and (b == True):
        return False
    elif(a == True) and (b == False):
        return False
    elif(a == True) and (b == True):
        return False
def main():
    print("| a | b | a nor b |")
    print("------------------")
    for a in [False, True]:
        for b in [False, True]:
            print('|', a, '|' , b, '|', NOR(a, b), '|')
main()

# and
def AND(a, b):
    if a == True and b == True:
        return True
	else:
		return False
def main():
    print("| a | b | a and b |")
    print("------------------")
    for a in [True, True]:
        for b in [True, True]:
            print('|', a, '|' , b, '|', AND(a, b), '|')
main()

# nand
def NAND(a, b):
    if a == True and b == True:
        return False
    else:
        return True
def main():
    print("| a | b | a nand b |")
    print("------------------")
    for a in [False, True]:
        for b in [False, True]:
            print('|', a, '|' , b, '|', NAND(a, b), '|')
main()
