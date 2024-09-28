'''
Given a string s and a dictionary of strings wordDict, 
add spaces in s to construct a sentence where each word is a valid dictionary word. 
Return all such possible sentences in any order.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 
'''
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        results = []
        self.backtracking(s, word_set, [], 0, results)
        return results
    
    def backtracking(self, s, word_set, curr_sent, start, results):
        if len(s) == start:
            results.append(" ".join(curr_sent))
            return

        for end in range(start+1, len(s)+1):
            word = s[start:end]
            if word in word_set:
                curr_sent.append(word)
                self.backtracking(s,word_set,curr_sent,end,results)
                curr_sent.pop()