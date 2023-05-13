# can only find middle one if count of target has more than one
def binary_search(arr: list, target: int):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = int(left + (right - left)/2) # (left + right)/2 可能會 整數溢出
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    
    return -1

if __name__ == "__main__":
    arr = [1, 3, 4, 5, 5, 7, 8, 11, 21]
    target = 9

    print(binary_search(arr, target))
        