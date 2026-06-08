# Key Learnings:

# Strings are immutable in Python → convert to list first
# Use chars[l], chars[r] = chars[r], chars[l] for swapping (no swap() function in Python)
# "".join(chars) joins list back into string with no separator


# Key Learnings:

# No need to reverse — just compare characters from both ends
# If any mismatch → return False immediately
# If loop completes → return True



# Key Learnings:

# if ch in 'aeiou' is cleaner than writing all 5 conditions with or
# in keyword works for strings, lists, and dictionaries
# Use else to count consonants, not a separate if



# Key Learnings:

# Use a dictionary {} to store character counts
# freq.get(key, 0) returns 0 if key doesn't exist yet
# for i in s → i is the character
# for i in range(len(s)) → i is the index, use s[i]

# ______________________________________________________
# Syntax Cheatsheet — Day 5

# # Swap two elements in a list
# a, b = b, a

# # Join list to string
# "".join(['h','e','l','l','o'])   # → "hello"

# # Check character in string
# if ch in 'aeiou': ...

# # Dictionary get with default
# freq.get(key, 0)

# # Loop by character vs index
# for ch in s:              # ch is the character
# for i in range(len(s)):   # i is the index → use s[i]

# # in keyword works everywhere
# if x in 'aeiou': ...      # string
# if x in [1,2,3]: ...      # list
# if x in dict: ...         # dictionary
# ______________________________________________________