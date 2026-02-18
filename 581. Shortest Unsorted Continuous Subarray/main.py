from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        n = len ( nums )

        maior = nums [ 0 ]

        menor = nums [ n - 1 ]

        right, left = 0, 0


        for i in range ( n ):

            if nums [ i ] >= maior:

                maior = nums [ i ]
            else:

                right = i 

            if nums [ n - i - 1 ] <= menor:

                menor = nums [ n -i - 1]

            else:

                left = n - i - 1

        
        return right - left + 1 if right != 0 or left != 0 else 0







        
    
            

            

            






            


s = Solution ()

nums = [ 1, 3, 2, 2, 2]

print ( s.findUnsortedSubarray( nums))


        
       