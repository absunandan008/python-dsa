"""
Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""

class Solution:
    def wordBreak_dfs(self, s: str, wordDict: List[str]) -> bool:
        wordDict_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]

            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict_set and dfs(end):
                    memo[start] = True
                    return True
            memo[start] = False
            return False
        return dfs(0)

    def wordBreak_dp(self, s: str, wordDict: List[str]) -> bool:
        wordDict_set = set(wordDict)
        dp = [False for _ in range(len(s)+1)]

        #we set initial to true because empty is true
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict_set:
                    dp[i] = True
                    break

        return dp[-1]
