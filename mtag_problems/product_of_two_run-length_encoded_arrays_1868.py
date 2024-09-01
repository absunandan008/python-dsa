"""
Run-length encoding is a compression algorithm that allows
for an integer array nums with many segments of consecutive repeated numbers to be represented
by a (generally smaller) 2D array encoded.
Each encoded[i] = [vali, freqi] describes the ith segment of repeated numbers in nums
where vali is the value that is repeated freqi times.
"""
from typing import List


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:

        i,j = 0,0
        result = []

        while i < len(encoded1) and j < len(encoded2):
            value1, freq1 = encoded1[i]
            value2, freq2 = encoded2[j]

            product = value1*value2
            min_len = min(freq1,freq2)

            if result and result[-1][0] == product:
                result[-1][1] += min_len
            else:
                result.append([product,min_len])

            encoded1[i][1] -= min_len
            encoded2[j][1] -= min_len

            if encoded1[i][1] == 0:
                i+= 1

            if encoded2[j][1] == 0:
                j+= 1

        return result