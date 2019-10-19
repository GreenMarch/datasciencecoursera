class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer = m + n - 1
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[pointer] = nums2[j]
                j -= 1
                pointer -= 1
            else:
                nums1[pointer] = nums1[i]
                i -= 1
                pointer -= 1
        while j >= 0:
                nums1[pointer] = nums2[j]
                j -= 1
                pointer -= 1
