'''
Group Anagrams

Given an array of strings, group anagrams together.

Example:
  Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
  Output:
  [
    ["ate","eat","tea"],
    ["nat","tan"],
    ["bat"]
  ]

Note:
  All inputs will be in lowercase.
  The order of your output does not matter.
'''


class Solution:
    def groupAnagrams(self, strs=None):
        n = len(strs)
        m = dict()

        for i in range(n):
            s = ''.join(sorted(strs[i]))

            if s not in m:
                m[s] = [strs[i]]
            else:
                m[s].append(strs[i])

        return list(m.values())


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
