"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1

"""
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_time = sorted([x[0] for x in intervals])
        end_time = sorted([x[1] for x in intervals])
        
        max_cnt = 0
        curr_cout = 0
        s,e = 0,0
        
        while s<len(intervals):
            if start_time[s] < end_time[e]:
                curr_cout += 1
                max_cnt = max(max_cnt, curr_cout)
                s += 1
            else:
                curr_cout -= 1
                max_cnt = max(max_cnt, curr_cout)
                e += 1
        return max_cnt
        #O(NlogN)
        #O(N)

"""
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])

        #heap
        free_rooms = []

        # add rooms
        heapq.heappush(free_rooms,intervals[0][1])

        for i in intervals[1:]:
            #if next meeting start is after top of heap end of meeting
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            
            #now add the meeting
            heapq.heappush(free_rooms, i[1])
        
        return len(free_rooms)
"""