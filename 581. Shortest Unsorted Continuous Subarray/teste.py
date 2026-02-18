from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        tam = len ( nums )

        for i in range ( tam - 1, 0, -1):
            if nums [ i ] < nums [ i - 1]:
                for j in range ( i ):
                    if nums [ j ] > nums [ j + 1 ]:
                        return i - j + 1
        
        return 0
    
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        tam = len ( nums )

        first, last = -1, -1

        for i in range ( tam - 1):
            if ( nums [ i ] > nums [ i + 1]):
                if first == -1:
                    first = i
                    last = i + 1
                else:
                    last = i + 1
                nums[ i ], nums [ i + 1] = nums [ i + 1], nums [ i ]
        if first == -1:
            return 0
        else:
            return last - first + 1
        
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        tam = len ( nums )

        i = 0

        statFirst = False

        statSecond = False

        while i < tam - 1 and statFirst == False:
            if nums [ i ] > nums [ i + 1]:
                statFirst = True
            else:
                i += 1

        if statFirst == True:
            j = tam - 1

            while j >= 0 and statSecond == False:
                if nums [ j ] < nums [ j - 1]:
                    statSecond = True
                else:
                    j -= 1
        
        print ( f"{nums [ i ]} e {nums[ j ]}")
        if statFirst == False:
            return 0
        else:
            return j - i + 1
        
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        problems = 1

        i = 1

        maior = nums [ 0 ]

        while i < len ( nums ):

            if nums [ i ] < maior:
                problems += 1
            else:
                maior = nums [ i ]
            
            i += 1
        
        if problems == 1:
            return 0
        return problems
            
    

s = Solution ()

nums = [ 2, 6, 4, 8, 10, 9, 15]

print ( s.findUnsortedSubarray( nums))