class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = []
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        size, queue = self.size, self.queue
        queue.append(val*1.0)
        window_sum = sum(queue[-size:])
        return window_sum / min(len(queue), size)
        
"""
Complexity

Time Complexity: \mathcal{O}(N)O(N) where NN is the size of the moving window, since we need to retrieve NN elements from the queue at each invocation of next(val) function.
Space Complexity: \mathcal{O}(M)O(M), where MM is the length of the queue which would grow at each invocation of the next(val) function.
"""

    def __init__(self, size):
        self.size = size
        self.queue = collections.deque()
        # number of elements seen so far
        self.window_sum = 0
        self.count = 0
    
    def next(self, val):
        self.count += 1
        # calculate the new sum by shifting the window
        self.queue.append(val*1.0)
        tail = self.queue.popleft() if self.count > self.size else 0
        
        self.window_sum = self.window_sum - tail + val
        
        return self.window_sum / min(self.size, self.count)
        
"""
Complexity

Time Complexity: \mathcal{O}(1)O(1), as we explained in intuition.
Space Complexity: \mathcal{O}(N)O(N), where NN is the size of the moving window.

"""
