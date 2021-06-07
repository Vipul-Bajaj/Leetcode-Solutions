# [Home](./../..)/[Pony.ai](./..)/[Medium](./)/Lexicographical_Numbers
<h1>Lexicographical Numbers</h1>

<p>
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
<br>
You must write an algorithm that runs in O(n) time and uses O(1) extra space. 
</p>

<b>Example 1:</b>

    Input: n = 13
    Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
    
<b>Example 2:</b>

    Input: n = 2
    Output: [1,2]

<b>Constraints:</b>

- 1 <= n <= 5 * 104

<h2>Solution</h2>

```python
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
    
        def backtrack(cur):
            if (cur > n): return
            ans.append(cur)
            backtrack(cur * 10)
            if cur % 10 != 9:
                backtrack(cur + 1)

        backtrack(1)
        return ans
```
