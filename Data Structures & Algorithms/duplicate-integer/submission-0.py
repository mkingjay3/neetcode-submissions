class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i in nums: 
            a.add(i)
        return(len(a) != len(nums))