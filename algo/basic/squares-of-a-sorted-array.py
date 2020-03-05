class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([i**2 for i in A])

    def sortedSquares2(self, A):
        return list(map(lambda x: x**2, A))


data = [1,3,5, 7]
print(Solution().sortedSquares2(data))

