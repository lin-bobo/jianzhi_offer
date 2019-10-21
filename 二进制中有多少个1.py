# _*_ coding: utf-8 _*_
__author__ = "bobo"
__date__ = "2019/10/21 23:33"


class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        # write your code here
        if num == -1:
            return 32
        isMinus = False
        if num < 0:
            isMinus = True
            num = ~num + 1
        count = 0
        while num != 0:
            if num % 2 != 0:
                count += 1
            num = num >> 1
        if isMinus:
            return 32 - count
        return count
