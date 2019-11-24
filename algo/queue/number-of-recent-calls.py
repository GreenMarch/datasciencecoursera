class RecentCounter(object):

    def __init__(self):
        self.q = collections.deque()
    
    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
        
"""
input
["RecentCounter","ping","ping","ping","ping"]
[[],[1],[100],[3001],[3002]]
output
[null,1,2,3,3]

Complexity Analysis

Time Complexity: O(Q)O(Q), where QQ is the number of queries made.

Space Complexity: O(W)O(W), where W = 3000W=3000 is the size of the window we should scan for recent calls. In this problem, the complexity can be considered O(1)O(1).

"""
