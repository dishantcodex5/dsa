from typing import List

def lowerbound(arr: List[int], n: int, target: int) -> int:
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

if __name__ == "__main__":
    arr = [1, 2, 22, 43, 56]
    n = len(arr)
    target = 33
    ind = lowerbound(arr, n, target)

    print("The lower bound is at index:", ind)
