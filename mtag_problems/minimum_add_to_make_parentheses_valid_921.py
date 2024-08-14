"""
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.
"""

class Solution:
    #for any '(' para add +1 to balace
    # for any '(' para remove 1 from bala
    # if we reach a '(' where there is no ')' left then we increament answer by 1
    # if there is any '(' left , meaning bal count is left then add bal+ans and return answer
    def minAddToMakeValid(self, s: str) -> int:
        bal,ans = 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                bal += 1
            else:
                bal -= 1
            if bal == -1:
                bal = 0
                ans += 1
        return ans+bal