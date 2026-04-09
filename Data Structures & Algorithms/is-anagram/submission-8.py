class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        count_s = Counter(s)

        for c in t:
            if c not in count_s or count_s[c] <= 0:
                return False
            else:
                count_s[c] -= 1
        return True
            