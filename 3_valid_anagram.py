from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = defaultdict(int)
        
        for i in s:
            d[i]+=1

        for i in t:
            d[i]-=1

        for v in d.values():
            if v != 0:
                return False
        
        return True