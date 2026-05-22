from typing import List

def print_interval ( arr : List [ int ], l : int, r: int):

    print ( "Array desse Intervalo ")

    for i in range ( l, r + 1):

        print ( arr [ i ], end = " ")
    
    print ()


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def b_search ( l : int, r: int ) -> int:

            if l <= r:

                m = ( l + r) // 2

                left, mid, right = nums [ l ], nums [ m ], nums [ r ]

                if mid == target :
                    return m
                
                if target < mid :

                    if left <= mid:
                        if left <= target:
                            return b_search ( l, m -1)
                        else:
                            return b_search ( m + 1, r )
                    else:
                        return b_search ( l, m -1 )
                else:
                    if mid <= right:
                        if target <= right:
                           return b_search ( m + 1, r)
                        else:
                           return b_search ( l, m - 1)
                    else:
                       return b_search ( m + 1, r)
            
            return -1               
            
                        
        return b_search ( 0, len ( nums ) - 1)




        

s = Solution()

nums = [ 1, 2, 3, 8]

target = 8

print ( s.search ( nums, target))