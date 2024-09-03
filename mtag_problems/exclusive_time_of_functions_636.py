"""
On a single-threaded CPU, we execute a program containing n functions.
Each function has a unique ID between 0 and n-1.

Function calls are stored in a call stack: when a function call starts,
its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack.
The function whose ID is at the top of the stack is the current function being executed.
Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

You are given a list logs, where logs[i] represents
the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3"
means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2"
means a function call with function ID 1 ended at the end of timestamp 2.
Note that a function can be called multiple times, possibly recursively.

A function's exclusive time is the sum of execution times for all function calls in the program.
For example, if a function is called twice, one call executing for 2 time units
and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.

Return the exclusive time of each function in an array,
where the value at the ith index represents the exclusive time for the function with ID i.
"""
from typing import List


class Solution:  # revision, May 2024
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        ans, stack, prev_time = [0] * n, deque(), 0  # Example: ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end  :6", "0:end:7"]

        for log in logs:  # time-
            id, action, timestamp = log.split(":")              # id   action  stamp    ans    stack     prev_time
            id, timestamp = int(id), int(timestamp)             # ––––   ––––    ––––   –––––   –––––   ---------
                                                                # 0    start     0    [0,0]   [0]       0
            if action == "start":                               # 0    start     2    [2,0]   [0,0]     2
                if stack:                                       # 0     end      5    [6,0]   [0]       6
                    ans[stack[-1]] += timestamp - prev_time     # 1    start     6    [6,0]   [0,1]     6
                stack.append(id)                                # 1     end      6    [6,1]   [0]       7
                prev_time = timestamp                           # 0     end      7    [7,1]   []        8
            else:
                ans[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
            # print(id,action,timestamp, ans, stack)

        return ans

# O(N)
# O(N)