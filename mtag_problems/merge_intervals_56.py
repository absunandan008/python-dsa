class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        prev = []
        result = []
        intervals.sort()
        for u in range(len(intervals)):
            if prev != []:
                if prev[0][0] <= intervals[u][0] <= prev[0][1] and intervals[u][0] <= prev[0][1] <= intervals[u][1]:
                    # merge
                    prev[0][1] = intervals[u][1]
                elif intervals[u][0] <= prev[0][0] <= intervals[u][1] and prev[0][0] <= intervals[u][1] <= prev[0][1]:
                    # merge
                    prev[0][0] = intervals[u][0]
                elif prev[0][0] <= intervals[u][0] and intervals[u][1] <= prev[0][1]:
                    continue
                elif prev[0][0] >= intervals[u][0] and intervals[u][1] >= prev[0][1]:
                    prev[0] = (intervals[u])
                else:
                    result.append(prev[0])
                    prev[0] = (intervals[u])
            else:
                prev.append((intervals[u]))
        result.append(prev[0])
        return result


