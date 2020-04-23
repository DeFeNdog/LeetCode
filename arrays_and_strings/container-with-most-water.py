'''
Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a
point at coordinate (i, ai). n vertical lines are drawn such that the two
endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together
with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

'''


class Solution:
    def maxArea(self, cds=None):
        max_area = 0
        point_a = 0
        point_b = len(cds) - 1

        while point_a < point_b:
            if cds[point_a] < cds[point_b]:
                max_area = max(max_area, cds[point_a] * (point_b - point_a))
                point_a += 1
            else:
                max_area = max(max_area, cds[point_b] * (point_b - point_a))
                point_b -= 1
        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
