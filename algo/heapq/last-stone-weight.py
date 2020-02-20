from heapq import heappop, heappush, heapify


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        else:
            for i, v in enumerate(stones):
                stones[i] = v * -1
            heapify(stones)
            res = 0
            while len(stones) > 1:
                s1 = heappop(stones)
                s2 = heappop(stones)
                if s1 == s2:
                    continue
                else:
                    print(s1, s2)
                    res = s1 - s2  # @if s1 < s2 else s2 - s1
                    heappush(stones, res)
            if stones:
                return stones[0] * -1
            else:
                return 0


inputdata = [2,7,4,1,8,1]
print(Solution().lastStoneWeight(inputdata))
"""
1046. Last Stone Weight
Easy

234

13

Favorite

Share
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""
