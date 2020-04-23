'''
3Sum

Given an array nums of n integers, are there elements a, b, c in nums such
that a + b + c = 0? Find all unique triplets in the array which gives the sum
of zero.

Note: The solution set must not contain duplicate triplets.

Example:
    Given array nums = [-1, 0, 1, 2, -1, -4],

    A solution set is:

    [[-1,-1,2],[-1,0,1]]
'''


class Solution:
    def threeSum(self, a=None):
        n = len(a)
        a.sort()
        result = []

        for i in range(n - 2):

            if i > 0 and a[i] == a[i - 1]:
                continue

            low = i + 1
            high = n - 1
            s = 0 - a[i]
            while low < high:
                if a[low] + a[high] == s:
                    result.append([a[i], a[low], a[high]])
                    while low < high and a[low] == a[low + 1]:
                        low = low + 1
                    while low < high and a[high] == a[high - 1]:
                        high = high - 1
                    low = low + 1
                    high = high - 1
                elif a[low] + a[high] > s:
                    high = high - 1
                else:
                    low = low + 1

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
