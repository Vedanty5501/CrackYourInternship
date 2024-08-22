class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt = dict()
        for i in range(len(nums)):
            if nums[i] in dt:
                return [i,dt[nums[i]]]
            else:
                dt[target-nums[i]]=i
            