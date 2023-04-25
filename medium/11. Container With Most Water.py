class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        res = 0
        while right >= left:
            
            if height[right]>height[left]:
                res = max(res , (right-left) * height[left])
                left += 1
            else:
                res = max(res , (right-left) * height[right])
                right -= 1
        return res

'''
//超時
class Solution:
    def maxArea(self, height: List[int]) -> int:
        leng = 0
        h = 0
        max_container = 0
        for i in range(len(height)-1):
            for j in range(1,len(height)):
                leng = j-i
                h = min(height[j],height[i])
                if leng*h > max_container:
                    max_container = leng*h
#                    print(leng,h)
        return max_container
'''
