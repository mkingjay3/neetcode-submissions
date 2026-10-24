class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = target; 
        sets = dict() 
        sm = 0 
        bi = 0
        a = []
        for i, num in enumerate(nums):
            diff = target - num
            if(diff in sets):
                sm = min(i, sets[diff])
                bi = max(i, sets[diff])
                a.append(sm)
                a.append(bi)
                return(a)
            sets[num] = i


     


