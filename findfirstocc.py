def findFirstOcc(arr, x, n):
    low = 0
    high = n - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            ans = mid
            high = mid - 1  # go left to find earlier occurrence
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return ans

arr=[1, 2, 3, 7, 7, 12, 12, 12]
arr.sort()  # Binary Search needs sorted array
n = len(arr)
x = 12
first_index = findFirstOcc(arr, x, n)
print("The first occurrence is at index:", first_index)
