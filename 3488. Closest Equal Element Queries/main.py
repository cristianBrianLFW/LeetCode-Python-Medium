
from typing import List

class Solution:
    def binary_search ( self, key, l, r, nums):
        if l <= r:
            m = ( l + r )//2

            if nums [ m ] == key:
                return m
            elif nums [ m ] > key:
                return self.binary_search ( key, l, m - 1, nums)
            else:
                return self.binary_search ( key, m + 1, r, nums)
            
        return -1
                
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        def incremento ( i, l_arr ):

            if i + 1 < l_arr:
                return i + 1
            else:
                return 0
        
        def decrement ( i, l_arr ):
            if i - 1 >= 0:
                return i -1
            else:
                return l_arr -1

        d = {}


        for i in range ( len ( nums )):

            if nums [ i ] in d:
                d [ nums [ i ] ].append ( i )
            else:
                d[ nums [ i ] ] = [ i ]

        l = []

        for query in queries:
            arr =  d [ nums [ query ]]
            l_arr = len ( arr )
            if len ( arr ) < 2:
                l.append ( -1 )
            else:
                print ( arr )
                i = self.binary_search(query, 0, l_arr, arr)
                j = incremento(i, l_arr)
                k = decrement ( i, l_arr)
                l.append( min ( abs ( arr [i] - arr[j]), abs ( arr[i] - arr [k]), abs ( l_arr - arr[i] + arr[j]), abs ( l_arr - arr [ i ] + arr [ k ]))  )
                print (i, j, k )
                print ()

        return l


    




s = Solution()

nums = [1,3,1,4,1,3,2]

queries = [0,3,5]


print ( s.solveQueries(nums, queries))
