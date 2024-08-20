class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)):
            minn = i
            for j in range(i,len(nums)):
                if nums[j]<nums[minn]:
                    minn=j
            nums[i],nums[minn]=nums[minn],nums[i]
        