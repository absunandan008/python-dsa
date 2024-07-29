import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = {u: 0 for u in range(numCourses)}
        graphCourses = {u: [] for u in range(numCourses)}

        for courses, pre in prerequisites:
            inDegree[pre] += 1
            graphCourses[courses].append(pre)

        output = []

        preQueue = collections.deque(u for u in range(numCourses) if inDegree[u] == 0)

        while preQueue:
            data = preQueue.popleft()
            output.append(data)
            for connected in graphCourses[data]:
                inDegree[connected] -= 1
                if inDegree[connected] == 0:
                    preQueue.append(connected)
        if len(output) != len(graphCourses):
            return []
        else:
            output.reverse()
            return output