# [Home](./../..)/[ByteDance](./..)/[Medium](./)/Plus_One
<h1>Plus One</h1>

<p>
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
</p>
<p>
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
</p>
<p>
You may assume the integer does not contain any leading zero, except the number 0 itself.
</p>

<b>Example 1:</b>

    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
    
<b>Example 2:</b>

    Input: digits = [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.

<b>Constraints:</b>

- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9

<h2>Solution</h2>

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i]+=1
                return digits
        return [1]+digits
```
