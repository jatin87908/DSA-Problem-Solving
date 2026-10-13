
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        prefix = 0
        m = {0: 1}

        for i in range(n):
            prefix += nums[i]

            needed = prefix - k

            if needed in m:
                ans += m[needed]

            if prefix in m:
                m[prefix] += 1
            else:
                m[prefix] = 1

        return ans
