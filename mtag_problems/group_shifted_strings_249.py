"""
Perform the following shift operations on a string:

Right shift: Replace every letter with the successive letter of the English alphabet, where 'z' is replaced by 'a'.
For example, "abc" can be right-shifted to "bcd" or "xyz" can be right-shifted to "yza".
Left shift: Replace every letter with the preceding letter of the English alphabet, where 'a' is replaced by 'z'.
For example, "bcd" can be left-shifted to "abc" or "yza" can be left-shifted to "xyz".
We can keep shifting the string in both directions to form an endless shifting sequence.

For example, shift "abc" to form the sequence:
... <-> "abc" <-> "bcd" <-> ... <-> "xyz" <-> "yza" <-> .... <-> "zab" <-> "abc" <-> ...
You are given an array of strings strings, group together all strings[i] that belong to the same shifting sequence.
You may return the answer in any order.

Example 1:
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:
Input: strings = ["a"]
Output: [["a"]]

"""
from collections import defaultdict
from typing import List

from trees.problems.lca_236 import solution


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        answers = defaultdict(list)

        for string in strings:
            pattern = self.get_pattern(string)
            answers[pattern].append(string)
        return list(answers.values())

    def get_pattern(self, letter):
        if len(letter) == 1:
            return '0'
        pattern = [str(len(letter))]
        for i in range(1, len(letter)):
            diff = (ord(letter[i]) - ord(letter[i-1])) % 26
            pattern.append(str(diff))
        return ','.join(pattern)

letters = ["abc","bcd","acef","xyz","az","ba","a","z"]
s = Solution()
print(s.groupStrings(letters))