class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sor = sorted(nums)
        dic = {}
        for element in sor:
            if element not in dic:
                dic[element]=1
            else:
                dic[element]+=1
        di = dict( sorted (dic.items(), key= lambda x: x[1],reverse = True)) 
        li=[]
        for key in di.keys():
            li.append(key)
        return li[0]

    
        

        