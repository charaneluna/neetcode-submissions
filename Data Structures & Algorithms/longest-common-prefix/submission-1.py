class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ''
        i = 0
        current = 0
        mini = len(strs[0])
        nbr = 0
        if len(strs)==1:
            return strs[0]
        if len(strs)==0:
            return ''
        for element in strs : 
            current = len(element)
            mini = min (current,mini)   #find shortest string
            nbr+=1
        while i<mini : 
            prefi = strs[0]
            bol = True
            for word in strs[1:]:
                if word[i]!=prefi[i]:
                    bol = False
                    break
            if bol : 
                out += word[i]
                i+=1
            else:
                return out
        return out

            

            
        