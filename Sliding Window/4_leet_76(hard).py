####### hashmap bhi use kr skte ho

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0 or len(s) < len(t):
            return ""
        count = 0
        low = 0
        high = 0
        res = float('inf')
        start = 0
        frequency = {}
        
        for ch in t:                                    # store frequency of t
            frequency[ch] = frequency.get(ch, 0) + 1

        while high < len(s): 
            ch = s[high]

            
            if ch in frequency:    # ---------------> if character needed
                frequency[ch] -= 1

                
                if frequency[ch] >= 0:  # ---------------> valid required character found
                    count += 1
            high += 1
           
            while count == len(t):       # ---------------> full valid window found
                length = high - low
                
                if length < res:          # ---------------> smaller answer found
                    res = length
                    start = low
                
                left_char = s[low]         # ---------------> remove left character

                if left_char in frequency:
                    frequency[left_char] += 1
                   
                    if frequency[left_char] > 0:    # --------------->window becomes invalid
                        count -= 1
                low += 1

        if res == float('inf'):
            return ""

        return s[start : start + res]