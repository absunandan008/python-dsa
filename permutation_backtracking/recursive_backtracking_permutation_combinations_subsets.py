def permute(nums):
    # Base case: if nums is empty, there's only one permutation: the empty list
    if len(nums) == 0:
        return [[]]
    result = []
    #iterate over each element
    for i in range(len(nums)):
    # Pick the current element and form the remaining list without this element
        remaining = nums[:i] + nums[i+1:]
        # Recursively find the permutations of the remaining elements
        for p in permute(remaining):
            result.append([nums[i]]+p)

    return result

#print(permute([1, 2, 3]))


def combine(n, k):
    def backtrack(start, comb):
        # Base case: if the combination is of the correct size, add it to the result
        if len(comb) == k:
            result.append(list(comb))  # Make a copy
            return

        # Try adding each number from start to n
        for i in range(start, n + 1):
            comb.append(i)  # Choose the current number
            backtrack(i + 1, comb)  # Recurse with the next number
            comb.pop()  # Un-choose the current number (backtrack)

    result = []
    backtrack(1, [])
    return result


print(combine(4, 2))


def subsets(nums):
    def backtrack(index, current):
        # Base case: when the end of the array is reached, add the current subset
        if index == len(nums):
            result.append(list(current))
            return

        # Option 1: Include nums[index]
        current.append(nums[index])
        backtrack(index + 1, current)

        # Option 2: Exclude nums[index]
        current.pop()
        backtrack(index + 1, current)

    result = []
    backtrack(0, [])
    return result


#print(subsets([1, 2, 3]))

