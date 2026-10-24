class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = dict() 
        num = []
        for i in nums: 
            if( i not in dic):
                dic[i] = 1
            else: 
                dic[i] += 1
        
        for nums, c in dic.items():
            heapq.heappush(num, (c, nums))
            if(len(num)>k):
                heapq.heappop(num)
        final = []
        for i in num: 
            final.append(i[1])
        return(final)