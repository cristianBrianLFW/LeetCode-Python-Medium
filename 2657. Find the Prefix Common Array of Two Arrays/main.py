
from typing import List

class Solution:
    def findThePrefixarrommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        d = {}

        arr = [0] * len ( A )

        for i in range ( len ( A )):
            d [ A [ i ]] = i 

        for i in range ( len ( B )):
            if d [ B [ i ]] <= i:
                arr [ i ] += 1
            else:
                arr [ d [ B [ i ] ] ] += 1
        for i in range ( 1, len ( arr ) ):
            arr [ i ] += arr [ i - 1]
        
        return arr
    


A = [ 1, 3, 2, 4]

B = [ 3, 1, 2, 4]

s = Solution()

print ( s.findThePrefixarrommonArray ( A, B))
