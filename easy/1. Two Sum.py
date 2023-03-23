class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            other_num = target - nums[i]
            if other_num in seen:
                return [i,seen[other_num]]
            else:
                seen[nums[i]] = i;
