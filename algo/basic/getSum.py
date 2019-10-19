class myMath:
    def __init__(self, var1, var2):
        self.num_a = var1
        self.num_b = var2

    def twoSum(self):
        outcome = self.num_a + self.num_b
        return outcome


# test
print(myMath.twoSum(1,2))
