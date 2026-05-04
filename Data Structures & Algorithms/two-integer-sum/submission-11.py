class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_hash = {}
        
        for i, n in enumerate(nums):
            compliment = target - n
            if compliment not in nums_hash:
                nums_hash[n] = i
            else:
                return [nums_hash[compliment], i]