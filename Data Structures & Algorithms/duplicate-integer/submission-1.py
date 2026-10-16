from typing import Dict
from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen: Dict[int, bool] = dict()
        for x in nums:
            if x in seen:
                return True
            seen[x] = True
        return False
