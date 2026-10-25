class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        l,m,r = 0, 1, (len(nums) -1)
        output = []

        for i in range(len(nums)):
            #keep l stable, move m and r 
            if(i>0 and nums[i] == nums[i-1]):
                continue
            l = i
            m = i + 1
            r = len(nums) -1
            while(m<r):
                total = nums[m] + nums[l] + nums[r]
                if(total >0):
                    r -= 1
                elif(total <0):
                    m += 1
                else: 
                    output.append([nums[l],nums[m],nums[r]])
                    m += 1
        
        se = set()
        for i in output: 
            se.add(tuple(i))
        output = []
        for i in se: 
            output.append(i)
        return(output)

        