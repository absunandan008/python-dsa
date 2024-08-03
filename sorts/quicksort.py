def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + quicksort(middle) + quicksort(right)

# Example usage
arr = [3, 8, 2, 5, 1, 9, 4, 7]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)
# Time O(n log n), worst O(n^2)
# Space O(n)