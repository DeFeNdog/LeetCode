'''
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring
without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a
subsequence and not a substring.

'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        max_len, i = 0, 0
        index = [-1] * 128
        for j, c in enumerate(s):
            i = max(index[ord(c)], i)
            max_len = max(max_len, j - i + 1)
            index[ord(c)] = j + 1
        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    # print(s.lengthOfLongestSubstring("bbbbb"))
    # print(s.lengthOfLongestSubstring("pwwkew"))
