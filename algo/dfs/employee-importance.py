"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
# 690. Employee Importance, final
class Solution(object):
    def getImportance(self, employees, id):
        emap = {e.id: e for e in employees}
        def dfs(e_id):
            # if not eid:
            #     return 0
            e = emap[e_id]
            stack = []
            for sub_e_id in e.subordinates:
                # curr_imp = dfs(sub_e_id)
                stack.append(dfs(sub_e_id))
            return sum(stack) + e.importance if stack else e.importance
        return dfs(id)

class Solution(object):
    def getImportance(self, employees, id):
        emap = {e.id: e for e in employees}
        def dfs(e_id):
            # if not eid:
            #     return 0
            e = emap[e_id]
            stack = []
            importance_sum = e.importance
            for sub_e_id in e.subordinates:
                curr_imp = dfs(sub_e_id) # works for [[1, 5, [2, 3]], [2, 3, [4]], [3, 3, []], [4, 10, []]]
                #stack.append(dfs(sub_e_id))
                importance_sum += curr_imp
            return importance_sum
        return dfs(id)




# 690. Employee Importance
class Solution(object):
    def getImportance_dfs(self, employees, id):
        emap = {e.id: e for e in employees}
        def dfs(e_id):
            # if not eid:
            #     return 0
            e = emap[e_id]
            stack = []
            importance_sum = 0
            for e_id in e.subordinates:
                stack.append(dfs(e_id)) # missing one more layer for "4" in [[1, 5, [2, 3]], [2, 3, [4]], [3, 3, []], [4, 10, []]]
            return sum(dfs(e_id)) + e.importance if e.subordinates else e.importance
        return dfs(id)
"""
        def dfs(eid):
            employee = emap[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))
        return dfs(id)
        """
        
"""
690. Employee Importance
Easy

458

502

Favorite

Share
You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

Example 1:

Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
 

Note:

One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.
"""
