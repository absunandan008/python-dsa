from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minInWindow = prices[0]
        max_Profit = 0
        for u in range(len(prices)-1):
            if prices[u] < prices[u+1]:
                minInWindow = min(minInWindow,prices[u])
                max_Profit = max(max_Profit, prices[u+1] - minInWindow)
        return max_Profit