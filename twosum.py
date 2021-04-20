#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lenght_of_list = len(nums)
        if lenght_of_list == 0:
            print("Target not found")
        elif lenght_of_list == 2:
            return [0,1]
        else:
            twosum_list = {}
            for index, num in enumerate(nums):
                n = target - num
                if n not in twosum_list:
                    twosum_list[num] = index
                else:
                    return [twosum_list[n], index]
                
                
