<h1>Partition Labels</h1>

<p>
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

<b>Example 1:</b>

    Input: S = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

 
<b>Constraints:</b>

    S will have length in range [1, 500].
    S will consist of lowercase English letters ('a' to 'z') only.

<h2>Solution</h2>

```python
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_occurence = {}
        
        for idx,i in enumerate(S):
            if i not in last_occurence:
                last_occurence[i] = None
            last_occurence[i] = idx
        
        
        partitions = []
        idx = 0
        while idx < len(S):
            right = last_occurence[S[idx]]
            left = idx
            while left<=right:
                if last_occurence[S[left]]>right:
                    right=last_occurence[S[left]]
                left+=1
            partitions.append(right-idx+1)
            idx = left
        
        return partitions
```
