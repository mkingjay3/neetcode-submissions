class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join(filter(str.isalnum, s))
        new = new.lower()

        l, r = 0, len(new)-1
        for i in range(int(len(new)/2)):
            if(new[l] == new[r]):
                r -= 1
                l+= 1
            else: 
                return(False)
        return(True)
