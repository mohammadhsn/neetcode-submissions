from typing import Dict, Tuple



"""
example 1:

nums = [3,4,5,6]
slots = {
    3: [0],
    4: [1],
    5: [2],
    6: [3]
}

example 2:

nums = [5, 5]
slots = {
    5: 0
}

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        slots: Dict[int, int] = dict()
        for i in range(len(nums)):
            difference = target - nums[i]
            j = slots.get(difference)
            if j is not None and i != j:
                return [min(i, j), max(i, j)]
            slots[nums[i]] = i
        
        return []
