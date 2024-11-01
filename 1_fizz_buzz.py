from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            p = ""
            if i % 3 == 0:
                p += "Fizz"
            if i % 5 == 0:
                p += "Buzz"
            if p == "": res.append(str(i))
            else: res.append(p)
        return res