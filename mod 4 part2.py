
def insertion_sort(list1):
    for i in range(1, len(list1)):
        value = list1[i]
        j = i - 1
        while j >= 0 and value < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = value
    return list1
arr = []
length = int(input("Введите длину массива: "))
for i in range(0, length):
    element = int(input())
    arr.append(element)
insertion_sort(arr)
print("Отсортированный массив: ")
print(arr)