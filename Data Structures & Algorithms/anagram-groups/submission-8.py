class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = {}

        for s in strs:
            str_key = ("").join(sorted(s))
            if str_key not in anagram_dict:
                anagram_dict[str_key] = [s]
            else:
                anagram_dict[str_key].append(s)
        return list(anagram_dict.values())