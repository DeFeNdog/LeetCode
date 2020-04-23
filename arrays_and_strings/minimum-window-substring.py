'''
Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).

Example:
  Input: S = "ADOBECODEBANC", T = "ABC"
  Output: "BANC"

Note:
    If there is no such window in S that covers all characters in T, returnthe
    empty string "". If there is such window, you are guaranteed that there
    will always be only one unique minimum window in S.
'''
from sys import maxsize


class Solution:
    def minWindow(self, s='', t=''):

        if not s or not t:
            return ''

        sl = len(s)
        tl = len(t)

        if sl == 0 or tl == 0:
            return ''

        left, right, count = 0, 0, 0
        bank = [0 for l in range(256)]
        minSize = maxsize
        minString = ''

        # initialize bank
        for i in range(tl):
            bank[ord(t[i])] += 1

        while right < sl:

            if bank[ord(s[right])] > 0:
                count += 1

            bank[ord(s[right])] -= 1
            right += 1

            while count == tl:

                if minSize > right - left:
                    minSize = right - left
                    minString = s[left:right]

                bank[ord(s[left])] += 1

                if bank[ord(s[left])] > 0:
                    count -= 1

                left += 1

        return minString


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
