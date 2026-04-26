class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the two strings have the same amount of the same characters return true
        # else return false
        if len(s) != len(t):
            return False
        
        # add each character from each string into two different hash tables
        # as you iterate through one string
        first = {}
        second = {}
        for i in range(len(s)):
            first[s[i]] = 1 + first.get(s[i], 0)
            second[t[i]] = 1 + second.get(t[i], 0)
        
        if first == second:
            return True
        else:
            return False