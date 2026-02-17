class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        result = set()

        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k] ==0:
                        triplet = tuple(sorted([nums[i],nums[j],nums[k]]))
                        result.add(triplet)

        return [list(triplet) for triplet in result]
