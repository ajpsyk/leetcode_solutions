from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create hashTable // key is first unique ordering, value is list of anagrams to key
        hashTable = {}
        #create array of anagram groups
        groups = []


        #iterate over strings
        for s in strs:
            foundAnagram = False
            for key in hashTable:
                # if isAnagram(key, str)
                if self.isAnagram(key, str):
                    # hashTable at key, push str into list
                    hashTable[key].append(str)
            if not foundAnagram:
                hashTable[s] = []
        
        # create groups from hashTable
        # iterate over keys and values in hashTable
        for key, value in hashTable.items():
            # push key into hashTable at key list
            value.append[key]
            # push Hasthable at key list into array of anagram groups
            groups.append(value)

        
        #return anagram groups
        return groups
                
    # isAnagram helper, takes in two strings, outputs boolean
    def isAnagram(self, s, t) -> bool:
        # compares len
        if len(s) != len(t):
            return False
        # puts first string into set
        set_s = set(s)
        # iterate over second string char
        for i in set_s:
            # compare count of char in set and str
            if s.count(i) != t.count(i):
                return False
        return True
    