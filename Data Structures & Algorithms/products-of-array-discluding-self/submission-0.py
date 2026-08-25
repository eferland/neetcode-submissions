class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0)>1:
            return [0] * len(nums)
        totalproduct = 1
        for num in nums:
            if num != 0:
                totalproduct *= num
        ans = [0] * len(nums)
        if nums.count(0) == 1:
            ind = nums.index(0)
            ans[ind] = totalproduct
            return ans
        for i in range(len(nums)):
            ans[i] = int(totalproduct/nums[i])
        return ans
        