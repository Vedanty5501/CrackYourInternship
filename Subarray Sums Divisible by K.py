class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n==1:
            if nums[0]%k==0:
                return 1
            else:
                return 0
        pr_summ  = [0]*n
        cnt=0
        pr_summ[0]=nums[0]
        for i in range(1,n):
            pr_summ[i]=pr_summ[i-1]+nums[i]
        
        dt= dict()
        for i in range(n):
            if pr_summ[i]%k in dt:
                dt[pr_summ[i]%k]+=1
            else:
                dt[pr_summ[i]%k]=1
        
        for i in dt:
            if i==0:
                cnt+=dt[i]
            if dt[i]>1:
                cnt+=(dt[i]*(dt[i]-1))/2
        return int(cnt)