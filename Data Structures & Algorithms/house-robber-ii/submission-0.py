class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        n = len(nums)
        dpdidnt = [0]*n
        dpdid = [0]*n

        dpdidnt[0] = 0
        dpdid[0] = nums[0]
        dpdid[1] = nums[0]
        dpdidnt[1] = nums[1]

        for i in range(2, n):
            dpdidnt[i] = max(dpdidnt[i-1], nums[i]+dpdidnt[i-2])
            dpdid[i] = max(dpdid[i-1], nums[i]+dpdid[i-2]) if i<n-1 else dpdid[i-1]
        return max(dpdid[n-1], dpdidnt[n-1])



