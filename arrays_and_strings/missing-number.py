'''
Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
the one that is missing from the array.

Example 1:
    Input: [3,0,1]
    Output: 2

Example 2:
    Input: [9,6,4,2,3,5,7,0,1]
    Output: 8

Note:
    Your algorithm should run in linear runtime complexity. Could you implement
    it using only constant extra space complexity?
'''


class Solution:
    def missingNumber(self, nums):
        nums.sort()
        n = len(nums)

        if nums[-1] != n:
            return n
        elif nums[0] != 0:
            return 0

        for i in range(1, n):
            expected_num = nums[i - 1] + 1
            if nums[i] != expected_num:
                return expected_num


if __name__ == '__main__':
    s = Solution()

    # print(s.missingNumber([0]))
    # print(s.missingNumber([1]))
    # print(s.missingNumber([2]))
    # print(s.missingNumber([0, 2]))
    # print(s.missingNumber([0, 1]))
    # print(s.missingNumber([2]))
    # print(s.missingNumber([3, 0, 1]))
    # print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
