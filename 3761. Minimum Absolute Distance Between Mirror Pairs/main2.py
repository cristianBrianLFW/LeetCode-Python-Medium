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
    

        minn = -1
        m = -1

        d = {}

        for i, num in enumerate(nums):
            d [ num ] = [ i ]

        for i, num in enumerate ( nums ):

            key = reverse ( num )

            if key in d:
                if i not in d [ key ] and i < d [ key ][ 0 ]:
                    print ("oi")
                    if ( len ( d [ key ]) <= 1):
                        d [ key ].append ( i )
                        m = abs ( d [ key ][ 0 ] - i)
                    else:
                        m1 = abs ( d [ key ][ 0 ] - d [ key ][ 1 ] )
                        m2 = abs ( d [ key ][ 1 ] - 1)
                        if m2 < m1:
                            d [ key ][ 0 ] = d [ key ][ 1 ]
                            d [ key ][ 1 ] = i
                        m = min ( m1, m2)

                if minn == -1:
                    minn = m
                else:
                    minn = min ( minn, m)

        
        return minn
        
