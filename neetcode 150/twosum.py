class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hashmap:
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = hashmap.get(nums[i], i)



# nums = [4,5,6]
# target = 10
nums = [3,4,5,6]
target = 7
# nums = [5,5]
# target = 10
print(Solution().twoSum(nums, target))