#Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLength = 0
        found = set()
        #sliding window, left and right, if you found the element in right which is already in set
        # then remove it from set and then move the left window by 1
        for right in range(len(s)):
            while s[right] in found:
                found.remove(s[left])
                left += 1
            found.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        return maxLength

    def lengthOfLongestSubstringUsingDict(s: str) -> int:
        char_index = {}  # Dictionary to store the index of each character
        max_length = 0
        start = 0

        for end, char in enumerate(s):
            # If we've seen this character before and it's after our current start
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            else:
                max_length = max(max_length, end - start + 1)

            char_index[char] = end

        return max_length

    # Test the function
    test_cases = ["abcabcbb", "bbbbb", "pwwkew"]
    for case in test_cases:
        print(f"Input: {case}")
        print(f"Output: {lengthOfLongestSubstringUsingDict(case)}")
        print()
