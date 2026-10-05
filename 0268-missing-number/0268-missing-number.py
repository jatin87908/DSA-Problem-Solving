class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n= len(nums)
        arr = []

        for i in range (0,n+1):
            if i not in nums:
                return i
            