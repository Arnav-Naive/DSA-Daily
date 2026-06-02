class Solution:
    def firstUniqChar(self, s: str) -> int:
        f = {}

        for i in range(len(s)):
            f[s[i]] = f.get(s[i], 0) + 1

        for i in range(len(s)):
            if f[s[i]] == 1 :
                return i
        return -1