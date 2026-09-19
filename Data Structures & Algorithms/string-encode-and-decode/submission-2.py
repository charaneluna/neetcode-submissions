class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs : 
            s+= str(len(word))+'.'+str(word)
        return s


    def decode(self, s: str) -> List[str]:
        i = 0
        res =[]
        while i < len(s):
            length = ''
            while s[i]!= '.': 
                length += s[i]
                i+=1
            l = int(length)
            i+=1
            res.append(s[i:l+i])
            i+=l

        return res

