class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i in range(len(nums)):
            needed=target-nums[i]
            if needed in seen:
                return [i, seen.get(needed)]
            seen[nums[i]]=i
        return[]
        
