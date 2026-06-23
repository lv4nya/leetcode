#Given two strings s and t, return true if t is an anagram of s, 
#and false otherwise.

#Link:https://leetcode.com/problems/valid-anagram/
#Difficulty: easy
#Topic: Hashmap
#Time complexity: O(n)
#Space Complexity: O(n)



class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freqs={}
        freqt={}
        for char in s:
            freqs[char]=freqs.get(char, 0)+ 1
        for char in t:
            freqt[char]=freqt.get(char, 0)+ 1

        return (freqs==freqt)
        
