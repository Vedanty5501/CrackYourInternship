class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        nums.sort()
        for  i in range(n-2):
            if nums[i]>0:
                break
            if i!=0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while(l<r):
                if nums[l]+nums[r]==(-1*nums[i]):
                    ans.add(tuple([nums[i],nums[l],nums[r]]))
                    l+=1
                    r-=1
                elif nums[l]+nums[r]>(-1*nums[i]):
                    r=r-1
                else:
                    l=l+1
        return list(map(list,ans))