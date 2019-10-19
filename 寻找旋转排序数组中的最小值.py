# _*_ coding: utf-8 _*_
__author__ = "bobo"
__date__ = "2019/10/20 1:55"


class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):
        # write your code here
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        else:
            i = len(nums) // 2
            return min(self.findMin(nums[:i]), self.findMin(nums[i:]))
