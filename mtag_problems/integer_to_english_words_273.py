"""
Convert a non-negative integer num to its English words representation.
Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""

class Solution:
    def numberToWords(self, num: int) -> str:
        
        #base case
        if num == 0:
            return "Zero"
        
        #Arrays for data
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        thousands = ["", "Thousand", "Million", "Billion"]
        
        result = ""
        group_index = 0
        while num > 0:
            
            if num % 1000 != 0:
                group_value = ""
                part = num % 1000

                #handle hundreds
                if part >= 100:
                    group_value += ones[part // 100] + " Hundred "
                    part %= 100
                
                if part >= 20:
                    group_value += tens[part//10] + " "
                    part %= 10
                
                if part > 0:
                    group_value += ones[part] + " "
                
                #append scale thousands million billions
                group_value += thousands[group_index] + " "
                result = group_value + result
            
            num //= 1000
            group_index += 1
        
        return result.strip()                
        