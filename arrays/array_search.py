

# Linear search, takes O(n) time complexity, O(1) space complexity
def linear_search(arr, target):
    # Go through each entry of arr and find the target
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search, array has to be sorted to work. Time complexity O(log n), O(1) space complexity
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = int((right - left) / 2)
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1

arr = [1, 2, 3, 4, 5]
print(linear_search(arr, 3))  # Output: 2
print(binary_search(arr, 3))  # Output: 2
