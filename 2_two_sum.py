from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, i in enumerate(nums):
            if target - i in d:
                return [idx, d[target - i]]
            else:
                d[i] = idx

        return []