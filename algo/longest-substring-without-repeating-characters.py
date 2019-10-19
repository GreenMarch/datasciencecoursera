class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        r = 0
        l = 0
        out = 0
        while r < len(s):
            if s[r] not in d:
                d[s[r]] = 1
                r += 1
                out = max(out, r - l)
            else:
                del d[s[l]]
                l += 1
        return out
