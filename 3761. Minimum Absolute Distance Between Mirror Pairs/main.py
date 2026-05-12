
from typing import List

class Solution:

    def minMirrorPairDistance(self, nums: List[int]) -> int:

        def reverse ( x ):
            k = 0

            while x > 0:
                k *= 10
                k += ( x % 10 )
                x //= 10

            return k
        

        d = {}

        k = -1

        for i in range ( 1, len ( nums )):

            j = i - 1

            stat = False

            while j >= 0 and stat == False :

                stat = reverse ( nums [ j ]) == nums [ i ]

                if stat:
                    mod = abs ( i - j )
                    if k == -1:
                        k = mod
                    elif mod < k:
                        k = mod

                j -= 1

        return k


s = Solution()

nums = [120, 21]

print ( s.minMirrorPairDistance( nums))




        
            







