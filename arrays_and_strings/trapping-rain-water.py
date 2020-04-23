'''
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it is able to trap after raining.

https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''


class Solution:
    def trap(self, height=None):
        ans, current = 0, 0
        st = []

        while current < len(height):
            while (st and height[current] > height[st[-1]]):
                top = st[-1]
                st.pop()
                if not st:
                    break
                distance = current - st[-1] - 1
                bounded_height = min(height[current],
                                     height[st[-1]]) - height[top]
                ans += distance * bounded_height

            st.append(current)
            current += 1

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
