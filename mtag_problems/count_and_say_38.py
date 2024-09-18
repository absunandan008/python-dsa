"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works
by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character
and the number marking the count of the characters (length of the run). For example, to compress the string "3322251"
we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11".
Thus the compressed string becomes "23321511".
Given a positive integer n, return the nth element of the count-and-say sequence.

Example 1:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"

Example 2:
Input: n = 1
Output: "1"

Explanation:
This is the base case.
"""


class Solution:
    def countAndSay(self, n: int) -> str:
       if n == 1:
           return "1"
       curr = "1"
       for _ in range(n-1):
           next_term = ""
           count = 1
           for i in range(1, len(curr)):
               if curr[i] == curr[i-1]:
                   count += 1
               else:
                   next_term += str(count) + curr[i-1]
                   count = 1
           next_term += str(count) + curr[-1]
           curr = next_term

       return curr




# Test cases
solution = Solution()
for j in range(1, 6):
    print(f"n = {j}: {solution.countAndSay(j)}")
#print(f"n = {4}: {solution.countAndSay(4)}")


"""
        if n == 1:
                return "1"

            prev = self.countAndSay(n - 1)
            result = ""
            count = 1
            current = prev[0]

            for i in range(1, len(prev)):
                if prev[i] == current:
                    count += 1
                else:
                    result += str(count) + current
                    current = prev[i]
                    count = 1

            result += str(count) + current
            return result
        """