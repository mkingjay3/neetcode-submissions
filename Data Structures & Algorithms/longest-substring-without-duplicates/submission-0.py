class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets = set()
        l = 0
        length = 0
        for i in range(len(s)): 
            while(s[i] in sets):
                sets.remove(s[l])
                l +=  1
            sets.add(s[i])
            length = max(length, i-l+1)
        return(length)


            

            

            



        