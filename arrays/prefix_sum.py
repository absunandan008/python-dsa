def calculate_prefix_sum(arr):
    prefix_sum = [0] * (len(arr)+1)
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i-1]
    return prefix_sum

# Example usage
arr = [3, 1, 4, 1, 5, 9, 2, 6]
prefix_sum = calculate_prefix_sum(arr)
print("Prefix sum:",prefix_sum)

# Function to get sum of subarray from index i to j (inclusive)
def range_sum(i, j):
    return prefix_sum[j+1] - prefix_sum[i]

# Example queries
print(range_sum(0, 2))  # Sum of arr[0:3] = 3 + 1 + 4 = 8
print(range_sum(3, 6))  # Sum of arr[3:7] = 1 + 5 + 9 + 2 = 17