def permutate(nums):
    result  = [[]]  # Start with an empty permutation
    for num in nums:
        new_permutations = []
        # Iterate over result because for each existing permutation, we need to insert the new number at every position
        for perm in result:
            # For each position in the current permutation (plus one extra for the end of the list)
            for i in range(len(perm) + 1):
                # Create a new permutation by inserting 'num' at position 'i'
                new_permutations.append(perm[:i] + [num] + perm[i:])
        # Assign the newly created permutations back to result
        result = new_permutations
    return result

#print("Permutations of [1,2,3] :: ",permutate([1, 2, 3]))
def combine(n, k):
    """
    Given an array of numbers from 1 to n, find all combinations of k elements from this array.

    Approach:
    - Use a `combinations` list that starts with an empty list representing the base case (no elements selected).
    - For each number from 1 to n, add it to the current combinations (if the size remains ≤ k).
    - Finally, filter out only the combinations that have exactly k elements.
    """
    combinations = [[]] # Start with the base case: one empty combination
    # Loop through the number set [1, 2, ..., n]
    for i in range(1, n+1):
        new_combinations = []
        # Loop through all combinations formed so far
        for comb in combinations:
            # Only extend combinations whose length is less than k
            if len(comb) < k:
                new_combinations.append(comb+[i]) # Add the current number to the combination
        combinations += new_combinations
    # Add the newly created combinations
    final_result = []
    for comb in combinations:
        if len(comb) == k:
            final_result.append(comb)
    # Add the newly created combinations
    #return [comb for comb in combinations if len(comb) == k]
    return final_result


#print("combinations of [1,2,3,4] and length 2 :: ",combine(4, 2))

def subsets(nums):
    #define base case
    subsets = [[]]
    #for data in nums
    for num in nums:
        new_subsets = [] # Temporary list to hold new subsets
        #for each data in subset
        for curr in subsets:
            # Create a new subset by adding the current number to each existing subset
            new_subset = curr + [num]
            new_subsets.append(new_subset)
        ##append it to original
        subsets += new_subsets
    # Add all the new subsets to the subsets_list
    return subsets

print("subsets of [1,2,3] :: ",subsets([1, 2, 3]))


