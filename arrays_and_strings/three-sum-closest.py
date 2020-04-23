'''
3Sum Closest

Given an array nums of n integers and an integer target, find three integers
in nums such that the sum is closest to target. Return the sum of the three
integers. You may assume that each input would have exactly one solution.

Example:

    Given array nums = [-1, 2, 1, -4], and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''


class Solution:
    def threeSumClosest(self, a=None, target=None):
        a.sort()
        n = len(a)
        result = a[0] + a[1] + a[n - 1]

        for i in range(n - 2):

            low = i + 1
            high = n - 1

            while low < high:
                curr_sum = a[i] + a[low] + a[high]
                if curr_sum > target:
                    high = high - 1
                else:
                    low = low + 1

                if abs(curr_sum - target) < abs(result - target):
                    result = curr_sum

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
