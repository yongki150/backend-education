from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            _sum = nums[i] + nums[j]
            if _sum == target:
                ans = [i, j]
                return ans
            elif _sum > target:
                j -= 1
            else:
                i += 1
        return False


if __name__ == "__main__":
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]