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