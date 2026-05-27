# 76. Minimum Window Substring

# make 2 frequency arrays
# needed -> stores frequency of chars of t
# have   -> stores frequency of current window

# example:
# t = "AABC"
#
# needed['A'] = 2
# needed['B'] = 1
# needed['C'] = 1


# function:
# checks whether current window satisfies all needed chars

def sahi(have, needed):

    for i in range(256):

        # if any required char missing
        if have[i] < needed[i]:
            return False

    return True


# sliding window

low = 0

for high in range(n):

    # add current character into window
    have[s[high]] += 1


    # if valid window found
    while sahi(have, needed):

        length = high - low + 1


        # found smaller answer
        if length < res:

            res = length

            # store starting index
            start = low


        # shrink window from left
        have[s[low]] -= 1

        low += 1


# final answer
return substring(start, res)