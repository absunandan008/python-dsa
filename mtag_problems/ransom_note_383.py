"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using
the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

"""
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magzine_map = collections.Counter(magazine)
        ransom_note_map = collections.Counter(ransomNote)
        remaining = ransom_note_map - magzine_map
        if remaining:
            return False
        return True