#Question: Contains Duplicates
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Solution 1: Using built-in functions
        return (len(nums) != len(set(nums)))
    
        #Solution 2: Using  hashset()
        hashset = set()
        
        for n in nums:
            if n in hashset: #if the number already exists in the hashset, just return True
                return True
            hashset.add(n) #if the number is not in the hashset, add it
        return False
        