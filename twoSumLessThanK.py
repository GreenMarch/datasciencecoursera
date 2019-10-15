class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if len(A) < 2:
            return -1
        else:
            all_twosum = []
            for i in range(0, len(A) - 1):
                for j in range(i + 1, len(A)):
                    all_twosum.append(A[i] + A[j])
            good_list = [x for x in all_twosum if x < K]
            if len(good_list) < 1:
                return -1
            else:
                good_list.sort()
                return good_list[len(good_list) - 1]
