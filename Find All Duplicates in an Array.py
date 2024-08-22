class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        dt = dict()
        for i in nums:
            if i in dt:
                dt[i]+=1
                ans.append(i)
            else:
                dt[i]=1
        return ans