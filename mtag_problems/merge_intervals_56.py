class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        prev = []
        result = []
        intervals.sort()
        for u in range(len(intervals)):
            if prev != []:
                if prev[0][1] < intervals[u][0]:
                    result.append(prev[0])
                    prev[0] = intervals[u]
                else:
                    prev[0][1] = max(prev[0][1], intervals[u][1])
            else:
                prev.append((intervals[u]))
        result.append(prev[0])
        return result


