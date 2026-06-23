
# Pythonic DS way, time complexity --> O(n.k.log(k))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outs = dict()
        for elem in strs:
            outs.setdefault(''.join(sorted(elem)), []).append(elem)
        return list(outs.values())


# Algorithmic way, better time complexity --> O(n.k)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            groups[tuple(count)].append(word)

        return list(groups.values())