class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)

        # calculate the sum of the moving window
        window_sum = sum(queue[-size:])
        return window_sum / min(len(queue), size)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# ["MovingAverage","next","next","next","next"]
# [[2],[10],[20],[30],[40]]

size = 3
obj = MovingAverage(size)
param_1 = obj.next(10)
param_2 = obj.next(20)
param_3 = obj.next(30)
param_4 = obj.next(40)

print(param_1, param_2, param_3, param_4)

"""
346. Moving Average from Data Stream
Easy

507

54

Add to List

Share
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

"""