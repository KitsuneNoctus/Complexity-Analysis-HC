'''
You're given strings J representing the types of stones that are jewels, and S
representing the stones you have.  Each character in S is a type of stone you have.
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:

Input: J = "z", S = "ZZ"
Output: 0

Note:

    S and J will consist of letters and have length at most 50.
    The characters in J are distinct.


'''

def find_jewels(J, S):
    total = 0 #O(1)
    for char_jewel in J: #O(n)
        for char_comp in S: #O(n)
            if char_jewel == char_comp:
                total += 1 #O(1)
    return total


print(find_jewels("aA","aAAbbbb"))
print(find_jewels("z","ZZ"))
print(find_jewels("iUeI","iInbHuMN"))
