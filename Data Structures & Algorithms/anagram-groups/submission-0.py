"""



"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = defaultdict(list)
        for word in strs:
            fingerprint = [0] * 26
            for c in word:
                loc = ord(c) - ord('a')
                fingerprint[loc] += 1
            alphabet[tuple(fingerprint)].append(word)

        result = []
        for v in alphabet.values():
            result.append(v)
        return result
