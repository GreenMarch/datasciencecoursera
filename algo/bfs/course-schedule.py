from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        count = {}

        for i in prerequisites:
            pre[i[1]].append(i[0])
            count[i[0]] = count.get(i[0], 0) + 1

        queue = []
        for i in range(numCourses):
            if i not in count:
                queue.append(i)
        solution_count = 0
        while len(queue):
            solution_count += 1
            x = queue.pop(0)
            for n in pre[x]:
                count[n] -= 1
                if count[n] == 0:
                    del count[n]
                    queue.append(n)

        if solution_count == numCourses:
            return True
        return False
"""
207. Course Schedule
Medium

2768

141

Add to List

Share
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites."""