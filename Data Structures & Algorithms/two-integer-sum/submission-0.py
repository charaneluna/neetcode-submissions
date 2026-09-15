class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            dic = {}
            for i,j in enumerate(nums):
                dic[i]=j # i is the index from the original list and j is the actual number
            lis2 = sorted(nums)
            left = 0
            right = len(lis2)-1
            while left<right : 
                if lis2[left]+lis2[right]<target:
                        left+=1
                elif lis2[left]+lis2[right]>target :
                    right-=1
                else :
                    v1 = lis2[left]
                    v2 = lis2[right]
                    break
                
            out = []
            for key in dic.keys():
                if dic[key] == v1 or dic[key] == v2:
                    out.append(key)
            if len(out)!=2:
                return ['']
            elif out[0]==out[1]: 
                return ['']
            else:
                return sorted(out)
