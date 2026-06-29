class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicc = {}

        for i, n in enumerate(nums):
            if target-n in dicc:
                return [dicc[target-n],i]
            else:
                dicc[n] = []
                dicc[n] = i