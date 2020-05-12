class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stk = []


    def push(self, x: int) -> None:
        if len(self.stk) != self.max_size:
            self.stk.insert(0, x)

    def pop(self) -> int:
        if len(self.stk) == 0:
            return -1
        else:
            return self.stk.pop(0)

    def increment(self, k: int, val: int) -> None:
        """
        void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.
        :param k:
        :param val:
        :return:
        """
        # stk = [3,   1,  2]
        # idx = [-3, -2, -1]
        # k = 4
        # val = 1
        #
        length = len(self.stk)
        if length < k:
            k = length
        # Walk from the end backwards in the list
        print("k =", k)
        k += 1
        k = k * -1
        index = -1
        print("k =", k, "index =", index)
        while index > k:
            self.stk[index] = self.stk[index] + val
            index -= 1



# ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
# [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]





# Your CustomStack object will be instantiated and called as such:
maxSize = 3
obj = CustomStack(maxSize)

obj.push(1)
obj.push(2)
obj.pop()

obj.push(2)
obj.push(3)
obj.push(4)

obj.increment(5,100)
obj.increment(2,100)

print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())