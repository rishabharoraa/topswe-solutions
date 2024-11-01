from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]

        for i in range(1, len(strs)):
            common_prefix = self.intersection(common_prefix, strs[i])

        return common_prefix

            
    def intersection(self, a: int, b: int):
        if len(a) > len(b):
            a,b = b,a

        res = ""

        for i in range(len(a)):
            if a[i] == b[i]:
                res += a[i]
            else:
                break
        
        return res
