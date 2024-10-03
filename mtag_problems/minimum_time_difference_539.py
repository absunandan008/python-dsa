"""
Given a list of 24-hour clock time points in "HH:MM" format, 
return the minimum minutes difference between any two time-points in the list. 

Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
"""

from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        bucket = [False] * (24*60)
        first_index = 1500
        last_index = 0
        for timePoint in timePoints:
            h, m  = map(int, timePoint.split(":"))
            minutes = 60 * h + m
            first_index = min(minutes, first_index)
            last_index = max(minutes, last_index)
            if bucket[minutes]:
                return 0
            bucket[minutes] = True
        
        res = 24*60 - last_index + first_index
        prev = 1500
        for i in range(first_index, last_index+1):
            if bucket[i]:
                if prev != 1500:
                    res = min(res, i-prev)
                prev = i
        return res
        #O(N)
        #(N)
    
"""
        time_minutes = [int(time[:2]) * 60 + int(time[3:]) for time in timePoints]

        time_minutes.sort()

        #in case time loops
        ans = 24*60 - time_minutes[-1] + time_minutes[0]
        for i in range(len(time_minutes)-1):
            ans = min(time_minutes[i+1]-time_minutes[i], ans)
            if ans == 0:
                return 0
        
        return ans
        #O(NlogN)
        #O(N)
"""