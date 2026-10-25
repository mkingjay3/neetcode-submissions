class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        for i in range(int(len(numbers) - 1)): 
            val = numbers[l] + numbers[r]
            if(val > target):
                r -= 1
            elif(val < target):
                l += 1
            else: 
                lis = [] 
                lis.append(l+1)
                lis.append(r+1)
                return(lis)
        