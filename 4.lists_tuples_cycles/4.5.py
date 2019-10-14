# Определения типа треугольника  (равнобедренный, разносторонний, равносторонний)

a = int(input())
b = int(input())
c = int(input())
if a < 0 and b < 0 and c < 0 and (a>b+c) or (b>a+c) or (c>a+b):
    print("Не существует")
elif a == 0 and b == 0 and c == 0:
    print("Точка")
elif a == b == c:
    print("Равностороний")
elif a == b or a == c or b == c:
    print("Равнобедренный")
else:
    print("Разносторонний")