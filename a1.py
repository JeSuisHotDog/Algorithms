def insertionsort(lst: list) -> None:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

def selectionsort(lst: list) -> None:
    for i in range(len(lst) - 1):
        smallest_value = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[smallest_value]:
                smallest_value = j
        lst[i], lst[smallest_value] = lst[smallest_value], lst[i]

def linear_search(lst: list, element: object) -> int:
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1

def binary_search(lst: list, element: object):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == element:
            return mid
        if lst[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive(lst: list, element: object, low: int = 0, high: int = None) -> int:
    if high is None:
        high = len(lst) - 1
    if high < low:
        return -1
    else:
        mid = (low + high) // 2
        if lst[mid] == element:
            return mid
        if lst[mid] < element:
            return binary_search_recursive(lst,element, mid + 1, high)
        if lst[mid] > element:
            return binary_search_recursive(lst,element, low, mid - 1)
    return -1

def linear_search_recursive(lst: list, element: object, index: int = 0) -> int:
    if index >= len(lst):
        return -1
    if lst[index] == element:
        return index
    return linear_search_recursive(lst, element, index + 1)


def insertionsort_with_binary_search(lst: list) -> None:
    for i in range(1, len(lst)):
        key = lst[i]
        pos = binary_search_insert(lst, key, 0, i - 1)
        for j in range (i, pos, -1):
            lst[j] = lst[j-1]
        lst[pos] = key

def binary_search_insert(lst:list, key:object) -> int:
    return _binary_search_insert(lst,key,0, len(lst)-1)

def _binary_search_insert(lst:list,key:object,low:int, high:int) -> int:
    if low > high:
        return low
    mid = (low + high) // 2
    if lst[mid] < key:
        return _binary_search_insert(lst, key, mid + 1, high)
    else:
        return _binary_search_insert(lst, key, low, mid - 1)

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7]
    key = 6
    print(binary_search_recursive(lst,key))
