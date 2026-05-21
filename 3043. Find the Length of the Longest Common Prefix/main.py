from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:


        s = set ()

        for num in arr1:

            while num > 0:
                s.add ( num )
                num //= 10
        upper = 0

        for num in arr2:
            d = 0
            while num > 0:
                if num in s:
                    d += 1
                num //= 10
            if upper < d:
                upper = d
        
        return upper

        