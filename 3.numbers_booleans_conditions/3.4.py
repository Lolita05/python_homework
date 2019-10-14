# Вариация задачи FizzBuzz

a = int(input()) # задаем целое число
if a % 3 == 0 and a % 5 == 0: # делится на 15
    print("FizzBuzz")
elif a % 5 == 0: # делится на 5
    print("Buzz")
elif a % 3 == 0: # делится на 3
    print("Fizz")
else: # не делится ни на 3, ни на 5
    print(a)
