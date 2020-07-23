# 두 요소의 위치를 바꿔주는 helper function
def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]


def partition(arr, start, end):
    q = end
    s, b = start, start

    while s < q:
        if arr[s] <= arr[q]:
            swap(arr, s, b)
            b += 1
        s += 1

    swap(arr, q, b)
    q = b
    return q


def quicksort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    if end - start < 1:
        return

    pivot = partition(arr, start, end)
    quicksort(arr, start, pivot - 1)
    quicksort(arr, pivot + 1, end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3)
print(list3)
