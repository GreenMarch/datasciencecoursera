from heapq import nlargest, heappop, heappush


class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :param k: int
        :param W: int
        :param Profits: List[int]
        :param Capital: List[int]
        :return: int
        """
        # to speed up: if all projects are available
        if W >= max(Capital):
            return W + sum(nlargest(k, Profits))
        n = len(Profits)
        projects = [(Capital[i], Profits[i]) for i in range(n)]
        # sort the projects :
        # the most available (= the smallest capital) is the last one
        projects.sort(key=lambda x: -x[0])
        print("proj", projects)
        available = []
        while k > 0:
            # update available projects
            while projects and projects[-1][0] <= W:
                heappush(available, -projects.pop()[1])
                # available.append(-projects.pop()[1])
                print("k, proj, avail:", k, projects, available)
            # if there are available projects,
            # pick the most profitable one
            if available:
                print("available", available)
                W -= heappop(available)
                print("W", W)
            # not enough capital to start any projectk -=1
            else:
                break
            k -= 1


k = 2
W = 1
Profits = [1,2,3]
Capital = [0,1,1]

print(Solution().findMaximizedCapital(k, W, Profits, Capital))