with open("numsTask2.txt", "r") as file:
    numbers = list(map(float, file.read().split(";")))


#5;3;11.22;15;28;25.5;14.78;2;8;7;33;14.77;11.11
def heapify(arr, n, i):
    largest = i
    left_index = 2 * i + 1
    right_index = 2 * i + 2

    if left_index < n and arr[left_index] > arr[largest]:
        largest = left_index

    if right_index < n and arr[right_index] > arr[largest]:
        largest = right_index

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


heap_sort(numbers)

with open("numsTask2.txt", "w") as file:
    for i in numbers:
        file.write(str(i)+";")
