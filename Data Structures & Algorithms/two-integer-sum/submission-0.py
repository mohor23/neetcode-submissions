class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev={}
        for i in range(len(nums)):
            value=target-nums[i]
            if value in prev:
                return [prev[value],i]
            prev[nums[i]]=i
        return [-1,-1]    