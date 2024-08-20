class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        repeat = set()
        for i in nums:
            if i in repeat:
                return i
            else:
                repeat.add(i)
        return 0