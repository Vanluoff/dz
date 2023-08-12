from random import randint

b = []
for i in range(10):
    b.append(randint(1, 100))
b.sort()
print(b)


znachenie = int(input())

mid = len(b) // 2
minimal = 0
visoko = len(b) - 1

while b[mid] != znachenie and minimal <= visoko:
    if znachenie > b[mid]:
        minimal = mid + 1
    else:
        visoko = mid - 1
    mid = (minimal + visoko) // 2

if minimal > visoko:
    print("Такого значения нет")
else:
    print("i =", mid)