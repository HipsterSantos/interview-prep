#this solution use complement , so what is complement  = 
from typing import List

class Solution: 
    def __init__(self, nums: List[int], target:int)->List[int]:
        hash_table = {}
        for i,num  in  enumerate(nums):
            complement = target - num
            if complement in hash_table:
                return [hash_table[complement],i]
            hash_table[num] = i
            
            
#solution two by using generator 

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        return next(([num_to_index[target - num], i] for i, num in enumerate(nums) if (target - num) in num_to_index or num_to_index.setdefault(num, i)), None)

# Example usage:
solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)  # Output: [0, 1]

# we need to practice about generator  the in order to understand this approach used 

#this solution below is non-eficiente 
from typing import List 

class Solution:
    def twoSumIter(self, nums:List[int],targer:int)->List[int]:

#this an array problem   sum two sorted array

class Solution: 
    def sumTwoSortedArray(self, nums1: List[int], nums2: List[int]):
        if len(num1)>len(num2):
            num1,num2 = num2,num1
        m1,m2 = len(num1),len(num2)
        left,right,half = 0, m1,(m1+m2+1)//2
        
        while left <= right: 
            num1Medium = (left+right)//2
            num2Medium = half - num1Medium