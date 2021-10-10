class SparseVector:
    def __init__(self, nums: List[int]):
        self.val = {}
        for i, c in enumerate(nums):
            if c:
                self.val[i] = c
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for k, v in self.val.items():
            if k in vec.val:
                res += v*vec.val[k]
        
        return res
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
