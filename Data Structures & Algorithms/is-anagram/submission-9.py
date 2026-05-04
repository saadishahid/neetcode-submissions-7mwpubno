class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        char_count_s = {}
        for c in s:
            char_count_s[c] = char_count_s.get(c, 0) + 1
        
        for c in t:
            if c not in char_count_s or char_count_s[c] <= 0:
                return False
            else:
                char_count_s[c] -= 1
        return True

