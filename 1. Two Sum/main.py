class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    if not i == j:
                        return [i, j]