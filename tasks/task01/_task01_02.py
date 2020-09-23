from typing import List


def _Fuc(_list, tg):
    i,j = 0, len(_list) - 1
    while(i < j):
        _sum = _list[i] + _list[j]
        print(i, " ", j, "  ", _sum)
        if(_sum == tg):
            ans = [i, j]
            return ans
        elif(_sum > tg): #더한 값이 더 클 경우
            j -= 1
        else:
            i += 1
    return False #불가능함 


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i, j = 0, len(nums) - 1
        while(i < j):
            _sum = nums[i] + nums[j]
            print(i, " ", j, "  ", _sum)
            if(_sum == target):
                ans = [i, j]
                print(ans)
                return ans
            elif(_sum > target): #더한 값이 더 클 경우
                j -= 1
            else:
                i += 1
        return False #불가능함 



if __name__ == "__main__":
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
