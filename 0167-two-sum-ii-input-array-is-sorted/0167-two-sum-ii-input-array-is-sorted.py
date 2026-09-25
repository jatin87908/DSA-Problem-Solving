class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        dict1 = {}

        for i in range (n):
            rem= target - nums[i]
            if rem in dict1:
                return [dict1[rem]+1,i+1]
            dict1[nums[i]]=i