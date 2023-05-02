class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        val = 0
        for i in range(len(nums)):
            res = res * nums[i]
        if res > 0:
            val = 1
        elif res < 0:
            val = -1
        return val
      
      
''' other solution
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            elif nums[i] < 0:
                res = -res
        return res
'''
