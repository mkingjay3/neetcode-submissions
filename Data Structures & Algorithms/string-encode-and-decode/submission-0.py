class Solution:

    def encode(self, strs: List[str]) -> str:

        stri = "" 
        #use ! as the seperating 
        for i in range(len(strs)):
            stri += "" + str(len(strs[i])) + ","
        stri += "!"

        for i in range(len(strs)):
            stri += strs[i]
        return(stri)

    def decode(self, s: str) -> List[str]:

        stop = s.index("!")
        af = s[stop + 1:]
        be = s[:stop]
        le = []
        fin = []

        for i in be.split(","):
            if(i != ""):
                le.append(int(i))
        
        for i in le:
            fin.append(af[0:i])
            af = af[i:]
        return(fin)



