# Time Complexity: O(V + E), V is the number of vertices and E is the number of edges
# Space Complexity: O(V + E)
# Did this code successfully run on Leetcode: Yes

from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        
        dependencies = [0] * numCourses # space O(V)
        dependencies_map = {} # space O(V + E)

        for edge in prerequisites:   # Time O(E)
            dependent = edge[0]
            independent = edge[1]

            dependencies[dependent] += 1

            if independent in dependencies_map:
                dependencies_map[independent].append(dependent)
            else:
                dependencies_map[independent] = [dependent]
        
        queue = deque()
        queue_size = 0

        for index in range(numCourses): # Time O(V)
            if dependencies[index] == 0:
                queue.append(index)
                queue_size += 1
        
        while len(queue):    # Time O(V)
            popped = queue.popleft()
            popped_deps = []

            if popped in dependencies_map:
                popped_deps = dependencies_map[popped]

            for el in popped_deps:   # Time O(E)
                dependencies[el] -= 1
                if dependencies[el] == 0:
                    queue.append(el)
                    queue_size += 1

                    if queue_size == numCourses:
                        return True
        
        return False

