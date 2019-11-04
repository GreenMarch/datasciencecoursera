class Solution(object):
    def minWindow(self, s, t):
        if not t or not s:
            return ""
        from collections import Counter
        dict_t = Counter(t)
        required = len(dict_t)

        l, r = 0, 0
        formed = 0

        window_counts = {}    
        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None
    
        while r < len(s):
    
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
    
            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
    
            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]
    
                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
    
                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
    
                # Move the left pointer ahead, this would help to look for a new window.
                l += 1    
    
            # Keep expanding the window once we are done contracting.
            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
        
    
S = "ADOBECODEBANC"
T = "ABC"
Solution().minWindow(S, T)

"""
76. Minimum Window Substring
Hard

2989

214

Favorite

Share
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
