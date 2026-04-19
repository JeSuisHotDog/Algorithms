def linear_search(lst: list, element: object) -> int:
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1


def binary_search(lst: list, element: object) -> int:
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == element:
            return mid
        if element > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def selectionsort(lst: list) -> None:
    for i in range(0, len(lst) - 1):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]


def insertionsort(lst: list) -> None:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


def partition_lomutos(lst: list, start: int, end: int) -> int:
    pivot = lst[end]
    i = start - 1
    for j in range(start, end):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[end] = lst[end], lst[i + 1]
    return i + 1


def quicksort_lomutos(lst: list) -> None:
    _quicksort_lomuts(lst, 0, len(lst) - 1)


def _quicksort_lomuts(lst, start, end):
    if start < end:
        pivot = partition_lomutos(lst, start, end)
        _quicksort_lomuts(lst, start, pivot - 1)
        _quicksort_lomuts(lst, pivot + 1, end)


def partition_hoares(lst: list, start: int, end: int) -> int:
    pivot = lst[start]
    i = start - 1
    j = end + 1
    while True:
        i += 1
        while lst[i] < pivot:
            i += 1
        j -= 1
        while lst[j] > pivot:
            j -= 1
        if i >= j:
            return j
        lst[i], lst[j] = lst[j], lst[i]


def quicksort_hoares(lst: list) -> None:
    _quicksort_hoares(lst, 0, len(lst) - 1)


def _quicksort_hoares(lst, start, end):
    if start < end:
        pivot = partition_hoares(lst, start, end)
        _quicksort_hoares(lst, start, pivot)
        _quicksort_hoares(lst, pivot + 1, end)


def merge(lst: list, left: list, right: list) -> None:
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1


def mergesort(lst: list) -> None:
    if len(lst) <= 1:
        return
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    mergesort(left)
    mergesort(right)
    merge(lst, right, left)


def heapify(lst: list, n: int, i: int) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and lst[left] > lst[largest]:
        largest = left
    if right < n and lst[right] > lst[largest]:
        largest = right
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)


def heapsort(lst: list) -> None:
    n = len(lst)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)
    for i in range(len(lst) - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, i, 0)


if __name__ == "__main__":
    lst = [9, 6, 3, 5, 8, 10, 15, 20]
    mergesort(lst)
    print(lst)
