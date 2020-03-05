class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:

        def find_first_one(A, lenRow, lenCol):
            for i in range(lenRow):
                for j in range(lenCol):
                    if A[i][j] == 1:
                        return i, j

        if not A:
            return 0

        lenRow, lenCol = len(A), len(A[0])

        queue = collections.deque()  # this queue is used just for iterate the first island
        visited = set()
        i, j = find_first_one(A, lenRow, lenCol)

        queue.append((i, j))
        visited.add((i, j))

        front = collections.deque()  # since the queue will be poped, this is the real queue used to save the frontier of island
        front.append((i, j))

        while queue:
            y, x = queue.popleft()
            for nxt_y, nxt_x in [(y + 1, x), (y, x + 1), (y - 1, x), (y, x - 1)]:
                if 0 <= nxt_y < lenRow and 0 <= nxt_x < lenCol and A[nxt_y][nxt_x] == 1 and (
                nxt_y, nxt_x) not in visited:
                    visited.add((nxt_y, nxt_x))
                    queue.append((nxt_y, nxt_x))
                    front.append((nxt_y, nxt_x))

        front.append('eol')

        dis = 0
        while (len(front) > 1):
            if front[0] == 'eol':
                dis = 1 + dis
                front.popleft()
                front.append('eol')
                continue

            y, x = front.popleft()
            for nxt_y, nxt_x in [(y + 1, x), (y, x + 1), (y - 1, x), (y, x - 1)]:
                if 0 <= nxt_y < lenRow and 0 <= nxt_x < lenCol and A[nxt_y][nxt_x] == 1 and (
                nxt_y, nxt_x) not in visited:
                    return dis
                if 0 <= nxt_y < lenRow and 0 <= nxt_x < lenCol and A[nxt_y][nxt_x] == 0 and (
                nxt_y, nxt_x) not in visited:
                    visited.add((nxt_y, nxt_x))
                    front.append((nxt_y, nxt_x))

"""
934. Shortest Bridge
Medium

500

40

Add to List

Share
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

Example 1:

Input: [[0,1],[1,0]]
Output: 1
Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Note:

1 <= A.length = A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
 """