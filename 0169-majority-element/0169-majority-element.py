class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dict1= {}
        n = len(nums)

        for num in nums: 
            if num not in dict1: 
                dict1[num] =1 
            else: 
                dict1 [num]+=1 

            if dict1 [num]> n/2:
                return num
        