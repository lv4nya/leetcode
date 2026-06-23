#Leetcode 49 Group Anagrams
#link: https://leetcode.com/problems/group-anagrams/
#difficult: Medium
#topics: Hash table, sorting
#time complexity: (i) O(m*n)  (ii) O(n * mlogm )     // n = number of words
#space complexity: (i) O(n)   (ii) O(n*m)            // m = number of chars in each word


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        #APPROACH ONE: FREQUENCY TUPLE        
        result=defaultdict(list)

        for word in strs:
            count = [0]*26
            for c in word:
                count[(ord(c) - ord("a"))] +=1

            result[tuple(count)].append(word)

        return result.values()

        #APPROACH TWO : SORTING KEY
        groups={}

        for word in strs:
            key=''.join(sorted(word))
            groups.setdefault(key, [] ).append(word)

        return list(groups.values())

  #### NOTE: while time complexity of method 1 is faster, method two performed better in the test cases provided by leetcode
