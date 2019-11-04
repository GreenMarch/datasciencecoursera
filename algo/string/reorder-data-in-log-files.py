class Solution:
    # pass
    def reorderLogFiles2(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """

        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)
    # not pass
    def reorderLogFiles(self, G):
        A = []
        B = []
        G = [i.split() for i in G] 
        for g in G:
            print(g[0])
            print(g[1])
            if g[1].isnumeric():
                A.append(g)
            else:
                B.append(g)
        final = [" ".join(i) for i in sorted(A, key = lambda x: x[1:] + [x[0]]) + B]
        return sorted(final)
"""
937. Reorder Data in Log Files
Easy

305

921

Favorite

Share
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 

Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""
