<h1>Group Anagrams</h1>

<p>
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

</p>

<b>Example 1:</b>

    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    
<b>Example 2:</b>

    Input: strs = [""]
    Output: [[""]]
    
<b>Example 3:</b>

    Input: strs = ["a"]
    Output: [["a"]]

<b>Constraints:</b>

- 1 <= strs.length <= 104
- 0 <= strs[i].length <= 100
- strs[i] consists of lower-case English letters.

<h2>Solution</h2>

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        anagrams = defaultdict(list)
        
        for s in strs:
            sorted_s = sorted(s)
            # print(sorted_s)
            anagrams["".join(sorted_s)].append(s)
        
        return anagrams.values()
```
