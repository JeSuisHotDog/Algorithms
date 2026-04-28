def countingsort(lst: list) -> None:
    B = lst[:]
    max_element = max(lst)
    C = [0 for x in range(max_element+1)]
    for element in lst:
        C[element] += 1
    for i in range(max_element):
        C[i+1] += C[i]
    for element in reversed(lst):
        C[element] -= 1
        B[C[element]] = element
    for i in range(len(B)) :
        lst[i] = B[i]

def radixsort_buckets(lst: list) -> None:
    max_val = max(lst)
    exp = 1
    while max_val // exp > 0:
        k = 0
        buckets = [[] for _ in range(10)]
        for num in lst:
            digit = (num // exp) % 10
            buckets[digit].append(num)
        for bucket in buckets:
            for num in bucket:
                lst[k] = num
                k += 1
        exp *= 10

def radixsort_counting(lst: list) -> None:
    max_val = max(lst)
    exp = 1
    while max_val // exp > 0:
        _countingsort(lst,exp)
        exp *= 10

def _countingsort(lst: list, exp: int) -> None:
    n = len(lst)
    B = [0] * n
    C = [0] * 10
    for i in range(n):
        digit = (lst[i] // exp) % 10
        C[digit] += 1
    for i in range(1, 10):
        C[i] += C[i-1]
    for i in reversed(range(n)):
        digit = (lst[i] // exp) % 10
        C[digit] -= 1
        B[C[digit]] = lst[i]
    for i in range(n):
        lst[i] = B[i]

def radixsort_strings(lst: list) -> None:
    max_len = max(len(s) for s in lst)
    for i in range(max_len -1,-1,-1):
        countingsort_strings(lst, i)

def countingsort_strings(lst:list,pos:int) -> None:
    n = len(lst)
    B = [''] * n
    C = [0] * 27
    for i in range(n):
        if pos < len(lst[i]):
            char = ord(lst[i][pos]) - ord('a') + 1
        else:
            char = 0
        C[char] += 1
    for i in range(1,27):
        C[i] += C[i-1]
    for i in reversed(range(n)):
        if pos < len(lst[i]):
            char = ord(lst[i][pos]) - ord('a') + 1
        else:
            char = 0
        C[char] -= 1
        B[C[char]] = lst[i]
    for i in range(n):
        lst[i] = B[i]

if __name__ == '__main__':
    lst = [9, 7, 5, 3, 1, 8, 6, 4, 2, 0]
    lst_words = ['d', 'ia', 'h', 'gg', 'f', 'e', 'd', 'cc', 'ab', 'ba']
    radixsort_strings(lst_words)
    print(lst_words)
