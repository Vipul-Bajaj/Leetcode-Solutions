# [Home](./../..)/[Facebook](./..)/[Medium](./)/Group_Shifted_Strings
<h1>Group Shifted Strings</h1>

<p>
We can shift a string by shifting each of its letters to its successive letter.
</p>

* For example, "abc" can be shifted to be "bcd".

<p>
We can keep shifting the string to form a sequence.
</p>

* For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".

<p>
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.
</p>

<b>Example 1:</b>

    Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
    Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
    
<b>Example 2:</b>

    Input: strings = ["a"]
    Output: [["a"]]

<b>Constraints:</b>

- 1 <= strings.length <= 200
- 1 <= strings[i].length <= 50
- strings[i] consists of lowercase English letters.

<h2>Solution</h2>

```python
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for s in strings:
            key = tuple([(ord(s[i])-ord(s[0]))%26 for i in range(len(s))])
            hash_map[key].append(s)
        out = []
        for v in hash_map.values():
            out.append(v)
        return out
```
