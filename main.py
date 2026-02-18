
from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        l = len ( nums )
        t = 0

        nums.sort ()

        i, j = 0, 0

        while i < l:
            if nums [ j ] * k  >= nums [ i ]:
                i += 1
            else:
                if i - j > t:
                    t = i - j 
                j += 1

        if i - j > t:
            t = i - j 

        return l - t if t != 0 else 0
        