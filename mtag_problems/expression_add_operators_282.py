"""
Given a string num that contains only digits and an integer target,
return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so
that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

Example 1:
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

Example 2:
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.

Example 3:
Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
"""
from multiprocessing.connection import answer_challenge
from typing import List

from linkedlist.problems.AddTwoNumbers_Optimal import current


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def backtrack(index, path, value, last):
            if index == len(num):
                # we have reached end of num, so now compare it with target
                if target == value:
                    result.append(path)
                return

            # now backtrack over everyhthing:
            for i in range(index, len(num)):
                if i != index and num[index] == '0':
                    break

                current = int(num[index:i + 1])

                # if first
                if index == 0:
                    backtrack(i + 1, path + str(current), current, current)
                else:
                    backtrack(i + 1, path + "+" + str(current), value + current, current)
                    backtrack(i + 1, path + "-" + str(current), value - current, -current)
                    backtrack(i + 1, path + "*" + str(current), value - last + last * current, last * current)

        backtrack(0, "", 0, 0)
        return result

