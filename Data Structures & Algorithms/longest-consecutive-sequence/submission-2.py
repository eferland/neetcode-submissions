class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dictionary = defaultdict(int)
        longest = 0
        for num in nums:
            if dictionary[num]==0:
                dictionary[num] = dictionary[num-1]+dictionary[num+1]+1
                dictionary[num-dictionary[num-1]] = dictionary[num]
                dictionary[num+dictionary[num+1]] = dictionary[num]
                longest = max(longest, dictionary[num])
        return longest
