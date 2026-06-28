
# 1. Check if a given year is a leap year.
# 2. Take a character and check if it’s a vowel or consonant.(shortcut)
# 3. Take a character and check whether it’s uppercase, lowercase, a digit, or a special
# character.  

------------------------------------------------------------------------

        if n % 4 == 0 and (n % 100 != 0 or n % 400 == 0):
            print("leap yr")
        else:
            print("not leap yr")

------------------------------------------------------------------------

          char = str(input("Enter char :"))
          if len(char) > 1:
            print("char length shoud be 1")
          else:
            char = char.lower()

          if char in 'aeiou':
              print("Vowel")
            else:
              if char.isalpha():
                print("Consonant")
              else:
                print("no letter")
------------------------------------------------------------------------

        s = input("Enter a character: ")

        # Ensure only one character is entered

        if len(s) != 1:
            print("Please enter exactly one character.")
        else:
            if s.isupper():
                print("Uppercase")
            elif s.islower():
                print("Lowercase")
            elif s.isdigit():
                print("Digit")
            elif not s.isalnum():  # Not a letter and not a number
                print("Special Character")
            else:
                # Handles cases like non-English letters that are alnum but not upper/lower/digit
                print("Other alphanumeric character")
