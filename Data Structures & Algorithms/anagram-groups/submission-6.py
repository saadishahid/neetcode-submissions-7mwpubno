class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = {}
        for c in strs:
            c_key = ("").join(sorted(c))
            if c_key not in anagram_dict:
                anagram_dict[c_key] = [c]
            else:
                anagram_dict[c_key].append(c)
        return list(anagram_dict.values())
