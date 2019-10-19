class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**10:
            return 0
        elif x >= 0:
            return self.reverse_pos(x)
        else:
            return self.reverse_pos(x*-1)*-1
        
    def reverse_pos(self, x):
        x_str = str(x)
        new_str_list = []
        for i in range(len(x_str)):
            new_str_list.append(x_str[len(x_str) - i - 1])
        new_str = "".join(new_str_list)
        return int(new_str)
