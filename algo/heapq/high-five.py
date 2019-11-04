
class Solution:
    def highFive2(self, items):
        import collections
        import heapq
        res = []
        data = collections.defaultdict(list)
        
        for id, score in items:
            heapq.heappush(data[id], score)
            
        for id, scores in data.items():
            avg = sum(heapq.nlargest(5, scores))//5
            res.append((id, avg,))
            
        return res
        

    def highFive(self, items):
        d = {}
        for i in items:
            if i[0] in d:
                d[i[0]].append(i[1])
            else:
                d[i[0]] = [i[1]]
        re = []
        for i in d:
            t = d[i]
            t.sort(reverse = True)
            s = sum(t[0:5])
            s = s//5
            re.append([i,s])
        return re
    
data = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Solution().highFive(data)
Solution().highFive2(data)

