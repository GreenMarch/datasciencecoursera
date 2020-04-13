class Solution:
    def trap(self, height):
        """
        :param height: List[int]
        :return: int
        """
        stack = []
        begin, result = 0, 0
        # while begin < len(height) and height[begin] == 0:
        #     begin += 1
        #     print("begin",begin)
        for i in range(begin, len(height)):
            print("i",i)
            print("current stk", stack)
            while stack and height[i] > height[stack[-1]]:
                print("in while loop")
                valley = height[stack.pop()]
                print("valley",valley)
                if stack:
                    result += min(height[i], height[stack[-1]] - valley) * (i - stack[-1] - 1)
                    print("i,stack peek",i,stack[-1])
                    print("width",i - stack[-1] - 1)
                    print("current stk 2", stack)
            stack.append(i)
            print("current stk 3", stack)
        return result

input = [2,1,0,1,3]
output = Solution().trap(input)
print(output)