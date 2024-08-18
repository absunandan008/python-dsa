from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        #mapofletter
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(index, path):
            #if path is same length as digits, we have correct combination
            if len(path) == len(digits):
                combinations.append(''.join(path))
                return #backtrack

            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index+1, path)
                path.pop()

        combinations = []
        backtrack(0, [])
        return combinations
    def letterCombinationsInitial(self, digits: str) -> List[str]:
        subsets = set()
        if not digits:
            return []
        map_number = {}
        map_number["2"] = ["a", "b", "c"]
        map_number["3"] = ["d", "e", "f"]
        map_number["4"] = ["g", "h", "i"]
        map_number["5"] = ["j", "k", "l"]
        map_number["6"] = ["m", "n", "o"]
        map_number["7"] = ["p", "q", "r", "s"]
        map_number["8"] = ["t", "u", "v"]
        map_number["9"] = ["w", "x", "y", "z"]
        n = len(digits)
        presubset = []
        for i in range(n):
            if digits[i] in map_number.keys():
                for value in map_number[digits[i]]:
                    presubset.append(value)

        # print(presubset)
        # print(digits)

        ##iterative
        '''
        result = [[]]
        for subs in presubset:
            tmp_subset = []
            for corr in result:
                tmp = corr + [subs]
                tmp_subset.append(tmp)
            result += tmp_subset
        '''

        ##backtracking
        result = []
        curr = []

        def backtracking(i):
            if i == len(presubset):
                if len(curr) == n:
                    # result.append(curr[:])
                    result.append(''.join(curr))
                return
            curr.append(presubset[i])
            backtracking(i + 1)
            curr.pop()
            backtracking(i + 1)

        backtracking(0)

        # print(result)
        for re in result:
            if len(re) == n:
                if all(re[i] in map_number[digits[i]] for i in range(n)):
                    subsets.add(''.join(re))

        return sorted(subsets, key=lambda x: x[0])
        '''
        for re in result:
            if len(re) == n:
                if n == 1 and re[0] in map_number[digits[0]]:
                    subsets.add(''.join(re))
                elif n == 2 and re[0] in map_number[digits[0]] and re[1] in map_number[digits[1]]:
                    subsets.add(''.join(re))
                elif n == 3 and re[0] in map_number[digits[0]] and re[1] in map_number[digits[1]] and re[2] in map_number[digits[2]]:
                    subsets.add(''.join(re))
                elif n == 4 and re[0] in map_number[digits[0]] and re[1] in map_number[digits[1]] and re[2] in map_number[digits[2]] and re[3] in map_number[digits[3]]:
                    subsets.add(''.join(re))
        sorted_subsets = sorted(subsets, key=lambda x: x[0])
        return sorted_subsets
        '''





