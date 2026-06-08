#Problem link:https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=plakya4j&
#Difficulty:easy
#Approach:Sliding Window
#Time complexity:O(n)
#Space complexity:O(1)


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen=set()
        left=0
        result=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            result=max(result, right-left+1)
        return result
        
        
