arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(arr, n):
    small = 0
    high = len(arr) - 1

    while small <= high:
        mid = (small + high) // 2
        shot = arr[mid]

        if shot == n:
            return mid
        if shot > n:
            high = mid - 1
        else:
            small = mid + 1
    return None


print(len(arr))
print(binary_search(arr, 3))
