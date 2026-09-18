class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for element in nums : 
            if element in dic.keys():
                dic[element]+=1
            else:
                dic[element]=1
        return sorted(dic, key=dic.get, reverse=True)[:k]