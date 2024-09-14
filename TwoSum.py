#Question: Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Solution 1: Brute Force
        #Time Complexity: O(n^2)
        #Space Complexity: O(n)
        outputlist = []
        for i in range(0,len(nums)):
            num = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==num:
                    outputlist.append(i)
                    outputlist.append(j)
                    return outputlist
        
        #Solution 2: Using hashmap
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        prevMap = {} # value : index
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[num]=i
        return