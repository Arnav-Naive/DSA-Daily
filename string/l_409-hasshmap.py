class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        f = {}

        # count frequency of each character
        for i in range(len(s)):
            f[s[i]] = f.get(s[i], 0) + 1

        res = 0
        odd = False

        for i in f:

            val = f[i]

            # if even, use full count
            if val % 2 == 0:
                res += val

            else:
                # odd count found
                odd = True

                # use val-1
                # example:
                # 5 -> use 4
                # 3 -> use 2
                res += val - 1

        # one odd character can sit in center
        if odd:
            return res + 1

        return res