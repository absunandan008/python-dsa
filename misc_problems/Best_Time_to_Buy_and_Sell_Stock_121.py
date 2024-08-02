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



    def maxProfitOptimized(self, prices: List[int]) -> int:

        left,right = 0,1
        mprofit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                mprofit = max(mprofit, prices[right] - prices[left])
            else:
                left = right
            right +=1
        return mprofit
