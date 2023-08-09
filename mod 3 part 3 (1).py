
def sq():
    a = int(input("Введите 1 сторону"))
    b = int(input('Введите 2 сторону'))
    c = int(input('Введите 3 сторону'))
    p = ((a + b + c) / 2)
    s1 = ((p * (p - a) * (p - b) * (p - c)) ** 0.5)
    print(s1)
sq()