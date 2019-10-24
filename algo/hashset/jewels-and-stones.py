class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # Approach #1: Brute Force [Accepted]
        
        # return sum(s in J for s in S) 
        
        # Time Complexity: O(J\text{.length} * S\text{.length}))O(J.length∗S.length)).
        # Space Complexity: O(1)O(1) additional space complexity in Python. In Java, this can be O(J\text{.length} * S\text{.length}))O(J.length∗S.length)) because of the creation of new arrays.
        # Approach #2: Hash Set [Accepted]
# Intuition and Algorithm

# For each stone, check whether it matches any of the jewels. We can check efficiently with a Hash Set.
        Jset = set(J)
        return sum(s in Jset for s in S)
    
#         Complexity Analysis
#         Time Complexity: O(J\text{.length} + S\text{.length}))O(J.length+S.length)). The O(J\text{.length})O(J.length) part comes from creating J. The O(S\text{.length})O(S.length) part comes from searching S.

#         Space Complexity: O(J\text{.length})O(J.length).
        
"""
771. Jewels and Stones
Easy

1627

302

Favorite

Share
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""
