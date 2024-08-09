def merge_three_sorted_arrays(arr1, arr2, arr3):
    # Initialize pointers for each array
    i, j, k = 0, 0, 0

    # Initialize the result array
    result = []

    # Continue until we've processed all elements from all arrays
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        # Find the smallest element among the current elements of the three arrays
        min_element = min(arr1[i], arr2[j], arr3[k])
        result.append(min_element)

        # Move the pointer of the array that contained the smallest element
        if min_element == arr1[i]:
            i += 1
        elif min_element == arr2[j]:
            j += 1
        else:
            k += 1

    # Process any remaining elements in arr1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    # Process any remaining elements in arr2
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    # Process any remaining elements in arr3
    while k < len(arr3):
        result.append(arr3[k])
        k += 1

    return result


# Example usage
arr1 = [ 1, 2, 41, 52, 84 ]
arr2 = [ 1, 2, 41, 52, 67 ]
arr3 = [ 1, 2, 41, 52, 67, 85 ]
#arr1 = [1, 4, 7, 9]
#arr2 = [2, 5, 8]
#arr3 = [3, 6, 10]
print(merge_three_sorted_arrays(arr1, arr2, arr3))