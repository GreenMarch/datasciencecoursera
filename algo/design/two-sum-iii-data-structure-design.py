class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.is_sorted = False

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums.append(number)
        self.is_sorted = False

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if not self.is_sorted:
            self.nums.sort()

        low, high = 0, len(self.nums) - 1
        while low < high:
            currSum = self.nums[low] + self.nums[high]
            if currSum < value:
                low += 1
            elif currSum > value:
                high -= 1
            else:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)