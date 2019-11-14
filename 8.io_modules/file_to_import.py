#Тут будет какой-то код :)


def greetings():
    print("Hey u do in")


def fibo(n):
    if n in (1, 2):
        return 1
    return fibo(n - 1) + fibo(n - 2)
