class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        arr = []
        k = k % len(nums)
        
        for i in range(len(nums) - k, len(nums)):
            arr.append(nums[i])
        
        for i in range(0, len(nums) - k):
            arr.append(nums[i])
                
                
        nums[:] = arr