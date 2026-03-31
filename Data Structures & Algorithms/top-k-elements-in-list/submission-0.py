class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)  # element -> frequency
        frequencies = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            frequency[num] += 1

        for num, freq in frequency.items():
            frequencies[freq].append(num)

        answer = []
        for i in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[i]:
                answer.append(num)
                if len(answer) == k:
                    return answer

        return answer

        