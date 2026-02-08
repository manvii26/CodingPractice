class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}

        for i, num in enumerate(nums):
            req = target - num


            if req in checked:
                return (checked[req],i)

            checked[num] =i
