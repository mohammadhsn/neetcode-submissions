from collections import defaultdict

from tabnanny import check
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        default_fn = int
        checksum = defaultdict(default_fn)
        for i in range(len(s)):
            checksum[s[i]] += 1
            checksum[t[i]] -= 1
        
        for v in checksum.values():
            if v != default_fn():
                return False
        return True
