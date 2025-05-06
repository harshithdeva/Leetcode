from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        real_gain = []
        start = 0
        real_gain.append(0)
        for g in gain:
            start += g
            real_gain.append(start)
        if real_gain:
            return max(real_gain)