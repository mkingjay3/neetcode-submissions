class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict() 
        stri = ""
        emp = [] 
        fin = []
        for i in strs:
            stri = "".join(sorted(i))
            if(stri not in dic):
                dic[stri] = [] 
                dic[stri].append(i)
                emp.append(stri)
            else:
                dic[stri].append(i)
            stri = ""
        ind = 0
        for i in emp:
            fin.append(dic[i])
        return(fin)