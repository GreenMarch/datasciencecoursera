class Solution:
    def reorderLogFiles(self, logs):
        def f(log):
            id, rest = log.split(" ", 1)
            print("id ", str(id))
            print("rest ", str(rest))
            return (0, rest, id) if rest[0].isalpha() else (1,)
        return sorted(logs, key=f)

    def reorderLogFiles2(self, logs):
        letters = []
        digits = []
        for log in logs:
            if log[-1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters = sorted(letters, key=lambda letter: (letter.split()[1:], letter.split()[0]))
        return letters + digits

    """
"letter.split()[0]" means identifier
"letter.split()[1:]" means content ignored identifier
"key=lambda letter: (letter.split()[1:],letter.split()[0])" has two sorting keys. 
    the first one "letter.split()[1:]" is priority 
    and second one "letter.split()[0]" is backup
Therefore, it means sort the letters array in lexicographical order and ignore identifier as priority, otherwise (for example two letters have same content)will keep the original order that is identifier order.
    
    
student_tuples = [
    ('A john', 'A', 15),
    ('B jane', 'B', 12),
    ('C dave', 'B', 10),
]

student_tuples = [
    'A john',
    'B mary',
    'C dave',
]

sorted(student_tuples, key=lambda student: (student.split()[1], student.split()[0]))



    """


"""
txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 2)

print(x)
"""
"""

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
