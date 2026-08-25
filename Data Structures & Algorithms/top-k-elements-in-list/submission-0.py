class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] +=1

        buckets = defaultdict(list)
        for key in count.keys():
            buckets[count[key]].append(key)

        temp = 0
        bucketindex = len(nums)
        output = []
        while temp<k:
            temp += len(buckets[bucketindex])
            output.extend(buckets[bucketindex])
            bucketindex -=1
        return output
