"""
In an alien language, surprisingly, they also use English lowercase letters,
but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographically in this alien language.

Basically a dictionary but we define the order
"""
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        # Create a diction with indexex or order
        # For each word check the index of next word for each letter
        # if any time next word is less than current word length then return false
        # if at some point letter do not match then see if the first is sorted
        # If yes then its sorted and break

        #OrderMap
        order_index = {}
        for index, val in enumerate(order):
            order_index[val] = index

        for i in range(len(words)-1):
            for j in range(len(words[i])):
                #if len of words is <= current then its false
                if j >= len(words[i+1]):
                    return False

                if words[i][j] != words[i+1][j]:
                    if order_index[words[i][j]] > order_index[words[i+1][j]]:
                        return False
                    break
        return True

