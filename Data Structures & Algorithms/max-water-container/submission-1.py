class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxs = 0 
        l, r = 0, len(heights) -1 

        while(l < r):
            height = min(heights[l], heights[r])
            width = abs(l-r)
            area = height * width 
            if(area < maxs):
                if(heights[l]<heights[r] or heights[l] == heights[r]):
                    l += 1
                else:
                    r -= 1
            else: 
                maxs = area
                if(heights[l]<heights[r] or heights[l] == heights[r]):
                    l += 1
                else:
                    r -= 1
                 
        return(maxs)

