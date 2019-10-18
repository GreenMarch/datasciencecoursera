class Solution:
    def romanToInt(self, s: str) -> int:
        my_hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        out = 0
        
        if "IV" in s or "IX" in s:
            out -= 2
        if "XL" in s or "XC" in s:
            out-= 20
        if "CD" in s or "CM" in s:
            out-= 200
            
        for i in s:
            out += my_hashmap.get(i)
        return out
