class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return(False)
        
        a = dict()
        for i in range(len(s)): 
            if(s[i] not in a):
                a[s[i]] = 1
            else: 
                a[s[i]] +=1

        for i in range(len(t)):
            if(t[i] not in a or a[t[i]] == 0):
                return(False)
            a[t[i]] -= 1

        return(True)