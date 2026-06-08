#Problem link:https://leetcode.com/problems/median-of-two-sorted-arrays/description/?envType=problem-list-v2&envId=plakya4j&
#Difficulty:hard
#Topic:?
#Approach: Merge sort
#Time complexity:O(m+n)
#Space complexity:O(n)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        #use merge sort
        def merge(nums1, nums2):
            i=0
            j=0
            merged=[]
            while i<len(nums1) and j<len(nums2):
                if nums1[i]<=nums2[j]:
                    merged.append(nums1[i])
                    i+=1
                else:
                    merged.append(nums2[j])
                    j+=1
                
            while j<len(nums2):
                merged.append(nums2[j])
                j+=1
            while i<len(nums1):
                merged.append(nums1[i])
                i+=1
            return merged

        merged=merge(nums1, nums2)
        size=len(merged)
        if size%2==0:
            ans=(merged[size/2]+merged[(size/2)-1])/2.0
        else:
            ans=(merged[size//2])

        return ans
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
