"""
Given a string s, return whether s is a valid number.

For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7",
"+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5",
"--6", "-+3", "95a54e53".

Formally, a valid number is defined using one of the following definitions:

An integer number followed by an optional exponent.
A decimal number followed by an optional exponent.
An integer number is defined with an optional sign '-' or '+' followed by digits.

A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

Digits followed by a dot '.'.
Digits followed by a dot '.' followed by digits.
A dot '.' followed by digits.
An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

The digits are defined as one or more digits.
"""
class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_dot = seen_exponent = False
        for i,c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in "+-":
                if i > 0 and s[i-1] not in "eE":
                    return False
            elif c in "eE":
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                #setting seen digit is false beacuse after exponent we start a new digit
                seen_digit = False
            elif c == ".":
                if seen_exponent or seen_dot:
                    return False
                seen_dot = True
            else:
                return False
        return seen_digit