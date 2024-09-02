class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k=j+1
                l = len(nums)-1
                while(k<l):
                    # if k==i or k==j:
                    #     i+=1
                    #     continue
                    # if l==i or l==j:
                    #     j-=1
                    #     continue
                    # print(i,j,k,l)
                    sm = nums[i]+nums[j]+nums[k]+nums[l]
                    if sm==target:
                        ans.add(tuple([nums[i],nums[j],nums[k],nums[l]]))
                        k+=1
                        l-=1
                    elif sm<target:
                        k+=1
                    else:
                        l-=1
        return list(map(list,ans))