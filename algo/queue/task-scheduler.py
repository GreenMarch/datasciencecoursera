class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)

        hs = collections.defaultdict(int)
        for task in tasks:
            hs[task] += 1

        count = 0
        cycle = n + 1

        heap = []

        for k, i in hs.iteritems():
            if i > 0:
                heapq.heappush(heap, (-i))                
        while heap:
            worktime = 0
            tmp = []
            for i in xrange(cycle):
                if heap:
                    tmp.append(heapq.heappop(heap))
                    worktime += 1
            # for cnt in tmp:
            #     cnt *= -1
            #     cnt -= 1
            #     if cnt > 0:
            #         heapq.heappush(heap, -cnt)
            for cnt in tmp:
                cnt += 1
                if cnt != 0:
                    heapq.heappush(heap, cnt)
            
            count += cycle if len(heap) > 0 else worktime

        return count

        
"""
621. Task Scheduler
Medium

2137

411

Favorite

Share
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Note:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""

"""
'''
idea behind solution

we first need to recognize that the most frequent occurring term determines the output
let A be the most frequent term (5 occurrences) and n = 3, then the solution would be in the form
of A___A___A___A___A??? where ___ represent less-frequent occurring terms or idles and ??? represent terms that occur
the exact same number of terms of the most frequent term. 

We simply find the maximum count of any task, subtract it by 1 (because the spot at the end (???) may or may not hold actual values), multiple that value by n, then add in the number of different terms that occurr the maximum number of times.

"""
class Solution(object):
    def leastInterval(self, tasks, n):
        frequencies = {} # used to count frequencies
        output = 0
        
        if n == 0:
            return len(tasks)
        
        # build word frequency dictionary
        for k in tasks:
            frequencies[k] = frequencies.get(k,0)+1
            
        max_value = max(frequencies.values()) # get the count of the most frequent occurring term
        
        # check if any other values occurred this same number of times
        max_value_occurrences = 0
        for value in frequencies.values():
            if value == max_value:
                max_value_occurrences += 1
                
        
        return max((max_value-1)*(n+1)+max_value_occurrences, len(tasks))
  """
