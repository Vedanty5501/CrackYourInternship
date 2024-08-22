class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        maxm = 0
        while(start<end):
            water = min(height[start],height[end])*(end-start)
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
            maxm = max(maxm,water)
        return maxm