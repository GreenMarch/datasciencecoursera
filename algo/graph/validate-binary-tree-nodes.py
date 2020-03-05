"""
Check for a tree by checking that there is exactly one root and all other nodes have exactly one parent and can be visited from that root.

Find if there is only one possible root first, then use BFS (or DFS) traversal to check if we can visit all nodes from that root. Use a set to track seen/visited nodes. Does not assume 0 is the root when it exists. See comments for details.

Complexities:
O(n) time
O(n) extra space: for set.

Note:
We can avoid the set subtraction in "root = (set(range(n)) - seen).pop()" by using an "unseen" set rather than a "seen" set. That way, at the end, for valid binary trees, "unseen" will have exactly the root. However, we would have to initialize with "unseen = set(range(n))". Personally, I feel it's easier to understand the solution using a "seen" set.
"""

import collections
class Solution:
    def validateBinaryTreeNodes(self, n, leftChild, rightChild) -> bool:
        """

        :param n: int
        :param leftChild: List[int]
        :param rightChild: List[int]
        :return: bool
        """

        # First, check for a root, ie, a node with no parents.
        # At the same time, check the necessary condition that there must be
        # exactly n-1 unique nonnegative values.  The root is the missing
        # nonnegative value.
        seen = set()

        for arr in (leftChild, rightChild):
            for x in arr:
                if x != -1:
                    if x in seen:  # has two parents
                        return False
                    seen.add(x)

        # If == n, then every node has a parent, so there are no roots.
        # If < n - 1, then there are more than one parentless node (ie, root),
        # or there are nodes with more than one parent (already returned).
        if len(seen) != n - 1:
            return False

        # Find the element that has not yet been seen.
        root = (set(range(n)) - seen).pop()  # only one possible element

        # Note: we still might have cases with:
        # - more than one component
        # - cycles
        # However, the component with the root cannot have a cycle.
        # If it did, there would be a node with two parents (a case we
        # already eliminated), or the root would have a parent (impossible
        # by how we picked a root by definition).  Self-cycles are also
        # eliminated...  Therefore, if we're able to visit every node from the
        # root, then this implies there is only one component and that there
        # are no cycles.

        # Now, check if we can visit all nodes from the root, using BFS.
        q = collections.deque([root])

        while q:
            x = q.popleft()
            n -= 1  # use parameter as reverse counter for num nodes visited

            if leftChild[x] != -1:
                q.append(leftChild[x])
            if rightChild[x] != -1:
                q.append(rightChild[x])

        # If n == 0, then we visited all n nodes.
        return n == 0

"""
1361. Validate Binary Tree Nodes
Medium

89

18

Add to List

Share
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

 

Example 1:



Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:



Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:



Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
Example 4:



Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false
 

Constraints:

1 <= n <= 10^4
leftChild.length == rightChild.length == n
-1 <= leftChild[i], rightChild[i] <= n - 1
"""