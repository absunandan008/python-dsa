class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        result = 0
        count_char = {}

        for right in range(len(s)):
            count_char[s[right]] = 1 + count_char.get(s[right], 0)
            currentLength = right - left + 1
            if currentLength - max(count_char.values()) <= k:
                result = max(result,currentLength)
            else:
                count_char[s[left]] -= 1
                left += 1
        return result