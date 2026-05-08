class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        str_x = str(x)

        i = 0
        j = len(str_x) - 1

        while i < j:
            if str_x[i] != str_x[j]:
                return False

            i += 1
            j -= 1

        return True