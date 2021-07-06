# [Home](./../..)/[Akuna Capital](./..)/[Medium](./)/Reduce_Array_Size_to_The_Half
<h1>Reduce Array Size to The Half</h1>

<p>
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.
</p>
<p>
Return the minimum size of the set so that at least half of the integers of the array are removed.
</p>

<b>Example 1:</b>

    Input: arr = [3,3,3,3,5,5,5,2,2,7]
    Output: 2
    Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
    Possible sets of size 2 are {3,5},{3,2},{5,2}.
    Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.
    
<b>Example 2:</b>

    Input: arr = [7,7,7,7,7,7]
    Output: 1
    Explanation: The only possible set you can choose is {7}. This will make the new array empty.
    
<b>Example 3:</b>

    Input: arr = [1,9]
    Output: 1
    
<b>Example 4:</b>

    Input: arr = [1000,1000,3,7]
    Output: 1   

<b>Constraints:</b>

- 1 <= arr.length <= 10^5
- arr.length is even.
- 1 <= arr[i] <= 10^5

<h2>Solution</h2>

```python
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        size = n = len(arr)
        count = Counter(arr)
        c=0
        for k,v in sorted(count.items(),reverse=True,key=lambda x:x[1]):
            n-=v
            c+=1
            if n<=size//2:
                return c
```
