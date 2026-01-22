class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        blank = []
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        for x in range(len(nums)):
            blank.append(hashmap[nums[x]])
        new_list = sorted(set(blank), reverse=False)
        # return new_list[-k:]
        # return sorted(set(blank))
        top_freq = new_list[-k:]
        answer = [        ]
        for keys in hashmap:
            if hashmap[keys] in top_freq:
                answer.append(keys)
        return answer

# nums = [1,2,2,3,3,3]
# k = 2
nums = [7,7]
k = 1
print(Solution().topKFrequent(nums, k))
