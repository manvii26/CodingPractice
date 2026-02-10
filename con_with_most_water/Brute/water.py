class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxArea = 0
        for i in range(n):
            for j in range(i+1,n):
                w = j-i
                curr_height = min(height[i],height[j])
                area = w*curr_height
                maxArea = max(area, maxArea)

        
        return maxArea
