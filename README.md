# Complexity Analysis - SPD 1.41
## Make School | SPD 1.41 | Complexity Analysis May 4, 2020

### Problem 1
[Problem Link](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)
#### Problem: Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
> Restate: Given a non-negative number, reduce the number to zero by dividing by 2 when even, and subtracting 1 when odd. Return the number of steps steps it takes.

[Solution](problem1.py)
#### Time Complexity:
O(n) - Linear Time - Single Loop used in entire solution, as well as singular assignments to variables.

#### Space Complexity:
Linear Space

### Problem 2
[Problem Link](https://leetcode.com/problems/jewels-and-stones/)
#### Problem: You're given strings J representing the types of stones that are jewels, and S representing the stones you have. Each character in S is a type of stone you have. You want to know how many of the stones you have are also jewels. The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
> Restate: Given two Strings J and S - J being the characters  that represent stones that are jewels, and S being the characters of stones you have, identify the number of stones in S that are Jewels. J will always have distinct letters. Take into account case sensitivity as well.

[Solution](problem2.py)
#### Time Complexity:
O(n^2) - Quadratic Time - Use of a nested for loop to go though both strings iteratively

#### Space Complexity:
Linear Space
