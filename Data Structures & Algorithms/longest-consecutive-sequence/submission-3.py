class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maximum = 0
        for num in numset:
            if not (num-1) in numset:
                test = 1
                while (num+test) in numset:
                    test += 1
                maximum = max(maximum, test)
        return maximum