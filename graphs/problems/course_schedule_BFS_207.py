import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #create a in degree map initialized to 0
        #only create with the number of courses needed
        in_degree = {u: 0 for u in range(numCourses)}

        #also make a graph becuase you want to know which are they connected to
        graph_courses = {u: [] for u in range(numCourses)}

        # populate graph and 0 degree as well
        for course,prereq in prerequisites:
            in_degree[prereq] += 1
            graph_courses[course].append(prereq)

        nodegree_queue =  collections.deque([i for i in in_degree if in_degree[i] == 0])

        topo_order = []

        while nodegree_queue:
            removenodegree = nodegree_queue.popleft()
            topo_order.append(removenodegree)

            for connection in graph_courses[removenodegree]:
                in_degree[connection] -= 1
                if in_degree[connection] == 0:
                    nodegree_queue.append(connection)

        if len(topo_order) != numCourses:
            return False
        else:
            return True


