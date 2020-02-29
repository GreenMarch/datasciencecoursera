class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
    """
    def judgeCircle(self, moves: str) -> bool:
        d = {
            'U':0,
            'D':0,
            'L':0,
            'R':0}
        for m in moves:
            d[m] += 1
        return d['U'] == d['D'] and d['L'] == d['R']
    """
