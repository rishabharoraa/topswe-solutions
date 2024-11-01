import math
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        temp = ''
        for i in range(math.floor(len(s) / 2)):
            temp = s[i]
            s[i] = s[len(s) - i - 1]
            s[len(s) - i - 1] = temp

