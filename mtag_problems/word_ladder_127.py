"""
A transformation sequence from word beginWord to word endWord using
a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList,
return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #edge cases
        if beginWord == endWord or not wordList or endWord not in wordList:
            return 0

        graph = defaultdict(list)

        # O(N*(M^2)). M is length of words
        for word in wordList:
            for i in range(len(word)):
                transform = word[:i] + "*" + word[i+1:]
                graph[transform].append(word)

        queue = deque([(beginWord, 1)])
        visited = set()

        while queue:
            word, distance = queue.popleft()
            if word == endWord:
                return distance
            visited.add(word)
            # O(N*(M^2)). M is length of words
            for i in range(len(word)):
                transform = word[:i] + "*" +word[i+1:]
                for t_w in graph[transform]:
                    if t_w not in visited:
                        queue.append((t_w, distance+1))

        return  0
        # O(N*(M^2))
        # (N*(M^2))
