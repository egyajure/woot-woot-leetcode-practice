class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for num in nums:
            freqs[num]+=1
        
        freq_to_num = defaultdict(list)
        # now map frequencies to nums
        for num, freq in freqs.items():
            freq_to_num[freq].append(num)

        # now go bucket by bucket
        ans = []
        for i in range(len(nums), 0, -1):
            for num in freq_to_num[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        
        return ans
        
        