class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        tam = len ( s )

        if tam == 0:
            return
        elif tam == 1:
            return s
        elif tam == 2:
            if s[ 0 ] == s [ 1 ]:
                return s
            else:
                return s [ 0 ]
        else:

            mid = tam // 2

            l, r = mid - 1, mid + 1

                    
        