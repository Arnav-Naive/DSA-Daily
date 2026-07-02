. Reverse String

. Valid Parentheses

. Remove All Adjacent Duplicates In String

503. Next Greater Element II (attempted only)

GFG - The Celebrity Problem    <https://www.geeksforgeeks.org/problems/the-celebrity-problem/1> -
--------------------------------------------------------------------------------------

🚀 Problem Statement: The Celebrity Problem

Ek party me $n$ log hain (numbered $0$ se $n-1$). Unme se ek Celebrity ho sakta hai.
Celebrity ki definition yeh hai:

1. Celebrity sabko jaanta hai? Nahi, Celebrity party me kisi ko nahi jaanta.

2. Celebrity ko sab jaante hain? Haan, party ka har ek insaan Celebrity ko jaanta hai.

Tumhe ek $n \times n$ binary matrix $M$ di jayegi, jahan:M[i][j] = 1 ka matlab hai: Insaan i, insaan j ko jaanta hai.M[i][j] = 0 ka matlab hai: Insaan i, insaan j ko nahi jaanta.

Task: Celebrity ka index return karo. Agar party me koi celebrity nahi hai, toh -1 return karo.

Example Matrix Analysis:

Matrix M:
    0  1  2  3  <- log (Columns)
0 | 0  0  0  1 |
1 | 0  0  1  1 |
2 | 1  0  0  1 |
3 | 0  0  0  0 |
^
log (Rows)

Row 0: M[0][3] = 1 -> $0$ jaanta hai $3$ ko.
Row 1: M[1][3] = 1 -> $1$ jaanta hai $3$ ko.
Row 2: M[2][3] = 1 -> $2$ jaanta hai $3$ ko.
Row 3: Saare elements 0 hain -> $3$ kisi ko nahi jaanta.
Yahan Insaan 3 dono conditions satisfy kar raha hai (sab usey jaante hain, aur wo kisi ko nahi jaanta).

Output: 3

--------------------------------------------------------------------------------------
