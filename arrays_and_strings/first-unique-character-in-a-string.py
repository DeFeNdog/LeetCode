'''
## First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's
index. If it doesn't exist, return -1.

Examples:
    s = "leetcode"
    return 0.

    s = "loveleetcode",
    return 2.

Note: You may assume the string contain only lowercase letters.
'''
from collections import Counter

hash
class Solution:
    def firstUniqChar(self, s):
        count = Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar("leetcode"))
    print(s.firstUniqChar("loveleetcode"))
