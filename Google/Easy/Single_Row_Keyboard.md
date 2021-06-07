# [Home](./../..)/[Google](./..)/[Easy](./)/Single_Row_Keyboard
<h1>Single-Row Keyboard</h1>

<p>
There is a special keyboard with all keys in a single row.
</p>
<p>
Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25). Initially, your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is |i - j|.
</p>
<p>
You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.
</p>

<b>Example 1:</b>

    Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
    Output: 4
    Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
    Total time = 2 + 1 + 1 = 4. 
    
<b>Example 2:</b>

    Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
    Output: 73

<b>Constraint:</b>
- keyboard.length == 26
- keyboard contains each English lowercase letter exactly once in some order.
- 1 <= word.length <= 104
- word[i] is an English lowercase letter.

<h2>Solution</h2>

```python
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hash_map = {}
        for i,ch in enumerate(keyboard):
            hash_map[ch] = i
        time = 0
        last = 0
        for ch in word:
            curr = hash_map[ch]
            time+=abs(curr-last)
            last = curr
        return time
```
