class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i in range(0, len(nums)) :
             nums[i] = int(nums[i])
        nums.sort()
        return str(nums[len(nums)-k])
