class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)

        low = 0

        # stores maximum answer
        res = 0

        # frequency dictionary
        freq = {}

        for high in range(n):

            # add current character into window
            freq[s[high]] = freq.get(s[high], 0) + 1

            # current window length
            length = high - low + 1

            # highest frequency character count
            # example:
            # AABAB
            # A -> 3
            # B -> 2
            # so maxCount = 3
            maxCount = max(freq.values())

            # how many replacements needed
            # example:
            # window length = 5
            # maxCount = 3
            # diff = 2
            # means replace 2 chars
            diff = length - maxCount

            # if replacements needed exceed k
            # shrink window
            while diff > k:

                # remove left character from window
                freq[s[low]] -= 1

                # move left pointer
                low += 1

                # recalculate length
                length = high - low + 1

                # recalculate max frequency
                maxCount = max(freq.values())

                # recalculate replacements needed
                diff = length - maxCount

            # update answer
            res = max(res, length)

        return res