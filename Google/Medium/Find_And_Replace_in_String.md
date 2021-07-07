# [Home](./../..)/[Google](./..)/[Medium](./)/Find_And_Replace_in_String
<h1>Find And Replace in String</h1>

<p>
You are given a 0-indexed string s that you must perform k replacement operations on. The replacement operations are given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.
<br>
To complete the ith replacement operation:
</p>

* Check if the substring sources[i] occurs at index indices[i] in the original string s.
* If it does not occur, do nothing.
* Otherwise if it does occur, replace that substring with targets[i].

<p>
For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this replacement will be "eeecd".
<br>
All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will not overlap.
</p>

* For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not be generated because the "ab" and "bc" replacements overlap.

<p>
Return the resulting string after performing all replacement operations on s.
<br>
A substring is a contiguous sequence of characters in a string.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2021/06/12/833-ex1.png">

    Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
    Output: "eeebffff"
    Explanation:
    "a" occurs at index 0 in s, so we replace it with "eee".
    "cd" occurs at index 2 in s, so we replace it with "ffff".
    
<b>Example 2:</b>    

<img src="https://assets.leetcode.com/uploads/2021/06/12/833-ex2-1.png">

    Input: s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
    Output: "eeecd"
    Explanation:
    "ab" occurs at index 0 in s, so we replace it with "eee".
    "ec" does not occur at index 2 in s, so we do nothing.

<b>Constraints:</b>

- 1 <= s.length <= 1000
- k == indices.length == sources.length == targets.length
- 1 <= k <= 100
- 0 <= indexes[i] < s.length
- 1 <= sources[i].length, targets[i].length <= 50
- s consists of only lowercase English letters.
- sources[i] and targets[i] consist of only lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def findReplaceString(self, s: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        for i,sr,t in sorted(zip(indexes,sources,targets),reverse=True):
            s = s[:i] + t + s[i+len(sr):] if s[i:i+len(sr)] == sr else s
        return s
```
