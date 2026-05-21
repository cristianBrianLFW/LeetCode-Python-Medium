from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len ( nums ) - 1

        def b_search ( l: int, r: int ) -> int:

            while l <= r:

                m = ( l + r ) // 2

                if nums [ m ] < nums [ r ]:

                    return b_search ( m + 1, r)
                else:
                    return b_search ( l, m - 1)
            return l
        
        return b_search ( l, r)

nums = [3,4,5,1,2]

s = Solution()

print ( s.findMin ( nums ))