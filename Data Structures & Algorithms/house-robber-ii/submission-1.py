from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]
        @cache 
        def f(i, end):
            if(i >= end):
                return(0)
            take = nums[i] + f(i+2, end)
            skip = f(i+1, end)
            return(max(take, skip))         
        return(max(f(0, n-1), f(1, n)))        