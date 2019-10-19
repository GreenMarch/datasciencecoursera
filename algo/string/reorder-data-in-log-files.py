class Solution:
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
