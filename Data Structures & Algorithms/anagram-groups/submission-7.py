class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = {}

        for s in strs:
            s_key = ("").join(sorted(s))
            if s_key in anagram_dict:
                anagram_dict[s_key].append(s)
            else:
                anagram_dict[s_key] = [s]
        return list(anagram_dict.values())