class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=3:
            return min(nums)
        left = n//4
        right = (3*n)//4
        if nums[left]<nums[right]:
            return self.findMin(nums[right:]+nums[:left+1])
        else:
            return self.findMin(nums[left:right+1])
