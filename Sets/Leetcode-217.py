#Given an integer array nums,
#return true if any value appears at least twice in the array, 
#and return false if every element is distinct.

#link: https://leetcode.com/problems/contains-duplicate/
#difficulty: Easy
#topic: Hashsets
#time complexity: O(n)
#space complexity:O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen=set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        
