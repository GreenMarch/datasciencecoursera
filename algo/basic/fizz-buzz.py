class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = [None]*n
        for i in range(n):
            if i < 2:
                out[i] = str(i + 1)
            elif (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                out[i] = "FizzBuzz"
            elif (i + 1) % 3 == 0 and (i + 1) % 5 != 0:
                out[i] = "Fizz"
            elif (i + 1) % 3 != 0 and (i + 1) % 5 == 0:
                out[i] = "Buzz"
            else:
                out[i] = str(i + 1)
                
        return out
