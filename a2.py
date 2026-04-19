def mergesort(lst: list) -> None:
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        mergesort(left)
        mergesort(right)
        merge(lst, left, right)


def merge(lst: list, left: list, right: list) -> None:
    i, j, k = 0, 0, 0
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

def mergesort_book(lst: list) -> None:
    _mergesort_book_helper(lst, 0, len(lst) - 1)


def _mergesort_book_helper(lst, p, r):
    if r <= p:
        return
    q = (p + r) // 2
    _mergesort_book_helper(lst, p, q)
    _mergesort_book_helper(lst, q + 1, r)
    merge_book(lst, p, q, r)


def merge_book(lst: list, start: int, mid: int, end: int) -> None:
    left = lst[start : mid + 1]
    right = lst[mid + 1 : end + 1]
    i = 0
    j = 0
    k = start
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
        i = i + 1
        k += 1
    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1


def quicksort_lomutos(lst: list) -> None:
    _quicksort_lomutos(lst, 0, len(lst) - 1)


def _quicksort_lomutos(lst: list, start: int, end: int) -> None:
    if start < end:
        pivot = partition_lomutos(lst, start, end)
        _quicksort_lomutos(lst, start, pivot - 1)
        _quicksort_lomutos(lst, pivot + 1, end)


def partition_lomutos(lst: list, start: int, end: int) -> int:
    pivot = lst[end]
    i = start - 1
    for j in range(start, end):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[end] = lst[end], lst[i+1]
    return i + 1


def quicksort_hoares(lst: list) -> None:
    _quicksort_hoares(lst, 0, len(lst) - 1)


def _quicksort_hoares(lst: list, start: int, end: int) -> int:
    if start < end:
        pivot = partition_hoares(lst, start, end)
        _quicksort_hoares(lst, start, pivot)
        _quicksort_hoares(lst, pivot + 1, end)


def partition_hoares(lst: list, start: int, end: int):
    i = start
    j = end
    pivot = lst[start]
    while True:
        while lst[i] < pivot:
            i += 1
        while lst[j] > pivot:
            j -= 1
        if i >= j:
            return j
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1


def heapsort(lst: list) -> None:
    n = len(lst)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)

    for i in range(n-1,0,-1):
        lst[0], lst[i] = lst[i], lst [0]
        heapify(lst, i, 0)


def heapify(lst: list, n: int, i: int):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and lst[left] > lst[largest]:
        largest = left
    if right < n and lst[right] > lst[largest]:
        largest = right
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)


def quicksort_hoares_improved(lst: list) -> None:
    _quicksort_hoares_improved(lst, 0, len(lst) - 1)


def _quicksort_hoares_improved(lst: list, start: int, end: int) -> int:
    if start < end:
        pivot = partition_hoares_improved(lst, start, end)
        _quicksort_hoares_improved(lst, start, pivot - 1)
        _quicksort_hoares_improved(lst, pivot + 1, end)

def partition_hoares_improved(lst, start, end):
    pivot = lst[end]
    j = end - 1
    i = start
    while True:
        while i < end and lst[i] < pivot:
            i += 1
        while j >= start and lst[j] > pivot:
            j -= 1
        if i >= j:
            lst[i], lst[end] = lst[end], lst[i]
            return i
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1

def quicksort_hoares_improved_median_3(lst: list) -> None:
    _quicksort_hoares_improved_median_3(lst, 0, len(lst) - 1)

def _quicksort_hoares_improved_median_3(lst, start, end):
    if start < end:
        median_idx = median_of_three(lst, start, end)
        if median_idx != end:
            lst[median_idx], lst[end] = lst[end], lst[median_idx]
        pivot = partition_hoares_improved(lst, start, end)
        _quicksort_hoares_improved_median_3(lst, start, pivot - 1)
        _quicksort_hoares_improved_median_3(lst, pivot + 1, end)

def median_of_three(lst: list, start: int, end: int) -> int:
    mid = (start + end) // 2
    if (lst[start] <= lst[mid] <= lst[end]) or (lst[start] >= lst[mid] >= lst[end]):
        return mid
    if (lst[mid] <= lst[start] <= lst[end]) or (lst[mid] >= lst[start] >= lst[end]):
        return start
    return end

if __name__ == '__main__':
    lst = [9, 7, 5, 3, 1, 8, 6, 4, 2, 0]
    quicksort_hoares_improved(lst)
    print(lst)