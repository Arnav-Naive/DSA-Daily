class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_len = 0

        for i in range(len(s)):
            seen = set()
            for char in s[i:]:        # i se end tak
                if char in seen:
                    break
                seen.add(char)
                max_len = max(max_len, len(seen))  # seen ki length?

        return max_len