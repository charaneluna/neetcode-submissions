class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1= {}
        dic2= {}
        for let in s :
            if let in dic1:
                dic1[let]+=1
            else:
                dic1[let]=1
        for let in t :
            if let in dic2:
                dic2[let]+=1
            else :
                dic2[let]=1           
        return dic1==dic2
        