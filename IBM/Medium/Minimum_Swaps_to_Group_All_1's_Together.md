# [Home](./../../..)/[IBM](./../..)/[Medium](./..)/Minimum_Swaps_to_Group_All_1's_Together
# [Home](./../../..)/[IBM](./../..)/[Medium](./..)/Minimum_Swaps_to_Group_All_1's_Together
<h1>Minimum Swaps to Group All 1's Together</h1>

<p>
Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

</p>

<b>Example 1:</b>

    Input: data = [1,0,1,0,1]
    Output: 1
    Explanation: 
    There are 3 ways to group all 1's together:
    [1,1,1,0,0] using 1 swap.
    [0,1,1,1,0] using 2 swaps.
    [0,0,1,1,1] using 1 swap.
    The minimum is 1.
    
<b>Example 2:</b>

    Input: data = [0,0,0,1,0]
    Output: 0
    Explanation: 
    Since there is only one 1 in the array, no swaps needed.
    
<b>Example 3:</b>

    Input: data = [1,0,1,0,1,0,0,1,1,0,1]
    Output: 3
    Explanation: 
    One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].

<b>Constraints:</b>

- 1 <= data.length <= 105
- data[i] is 0 or 1.

<h2>Solution</h2>

```python
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = len(data)
        num_of_ones = 0
        for i in data:
            if i == 1:
                num_of_ones +=1
        x = num_of_ones
        max_ones = -2**31
        
        precompute = [0]*n
        
        if data[0] == 1:
            precompute[0] = 1
        for i in range(1, n):
            if data[i] == 1:
                precompute[i] = precompute[i-1]+1
            else:
                precompute[i] = precompute[i-1]
                
        for i in range(x-1,n):
            if i == x-1:
                num_of_ones = precompute[i]
            else:
                num_of_ones = precompute[i] - precompute[i-x]
            if (max_ones < num_of_ones):
                max_ones = num_of_ones    
        return x-max_ones
```
