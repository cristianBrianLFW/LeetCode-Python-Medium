from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        l = len ( nums )
        t = 0

        nums.sort ()

        print ( nums )

        for i in range ( l ):
            print ( "numero atual --> ", nums [ i ])
            j = i + i
            while j < l and nums [ j ] <= nums [ i ] * k:
                print ( "numero sendo visto --> ", nums [ j ])
                print ( "valor do intervalo ", j - 1, end= "\n\n")
                j += 1
            if j - i > t:
                t = j - i

        return len ( nums ) - t
    

a = Solution()

b = [ 1, 6, 2, 9]

a.minRemoval(b, 3)