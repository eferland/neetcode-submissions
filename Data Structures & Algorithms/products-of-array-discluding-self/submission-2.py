class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        zeros = 0
        zindex = -1
        totalproduct = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros+=1
                if zeros>1:
                    return ans
                zindex = i
            else:
                totalproduct *= nums[i]
        if zeros == 1:
            ans[zindex] = totalproduct
            return ans
        for i in range(len(nums)):
            ans[i] = totalproduct//nums[i]
        return ans
        