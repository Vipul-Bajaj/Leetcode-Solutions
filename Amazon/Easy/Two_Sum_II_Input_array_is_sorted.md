# [Home](./../..)/[Amazon](./..)/[Easy](./)/Two_Sum_II_Input_array_is_sorted
<h1>Two Sum II - Input array is sorted</h1>

<p>
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
</p>
<p>
Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
</p>
<p>
The tests are generated such that there is exactly one solution. You may not use the same element twice.
</p>

<b>Example 1:</b>

    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
    
<b>Example 2:</b>

    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    
<b>Example 3:</b>

    Input: numbers = [-1,0], target = -1
    Output: [1,2]

<b>Constraints:</b>

- 2 <= numbers.length <= 3 * 104
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution.

<h2>Solution</h2>

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0,len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i]+numbers[j] > target:
                j-=1
            else:
                i+=1
```
