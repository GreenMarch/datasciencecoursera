from collections import deque

class Solution:
    def trap(self, height):
        """
        :param height: List[int]
        :return: int
        """
        ans = 0
        i = 0
        stack = []
        while i < len(height):
            # monotonic stack
            # if stack is empty or current height is lower than the top element of the stack
            # push the index into the stack
            if not stack or height[i] <= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                bottom = stack.pop()
                if not stack:
                    continue
                distance = i - stack[-1] - 1  # remember to decrease 1
                bounded_height = min(height[i], height[stack[-1]]) - height[bottom]
                ans += distance * bounded_height
        return ans

input = [0,1,0,2,1,0,1,3,2,1,2,1]
output = Solution().trap(input)
print(output)