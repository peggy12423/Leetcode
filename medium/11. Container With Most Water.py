class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0                //左邊索引值
        right = len(height) -1    //右邊索引值
        res = 0
        while right >= left:     //當左小於右索引值時
            
            if height[right]>height[left]:       //右值大於左值
                res = max(res , (right-left) * height[left])     //結果為兩者索引值相減*右值
                left += 1                                       //左索引值+1
            else:
                res = max(res , (right-left) * height[right])     //結果為兩者索引值相減*左值
                right -= 1                                        //右索引值-1
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
