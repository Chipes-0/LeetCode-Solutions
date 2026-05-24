class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                out.append("FizzBuzz")
                continue
            elif i % 5 == 0:
                out.append("Buzz") 
                continue
            elif i % 3 == 0:
                out.append("Fizz")
                continue
            out.append(str(i))
        return out