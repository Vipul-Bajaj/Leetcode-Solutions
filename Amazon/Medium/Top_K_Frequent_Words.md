<h1>Top K Frequent Words</h1>

<p>
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

<b>Example 1:</b>

    Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
    Output: ["i", "love"]
    Explanation: "i" and "love" are the two most frequent words.
        Note that "i" comes before "love" due to a lower alphabetical order.

<b>Example 2:</b>

    Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
    Output: ["the", "is", "sunny", "day"]
    Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
        with the number of occurrence being 4, 3, 2 and 1 respectively.
 
<b>Constraints:</b>

- You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
- Input words contain only lowercase letters.

<h2>Solution</h2>

```python
class Solution:
    def _comparator(self,left,right):
        if left[1]>right[1]:
            return -1
        if left[1]<right[1]:
            return 1
        if left[0]>right[0]:
            return 1
        if left[0]<right[0]:
            return -1

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = defaultdict(int)
        
        for word in words:
            word_count[word]+=1
        
        word_count = sorted(word_count.items(),key=cmp_to_key(self._comparator))
        
        return [word_count[i][0] for i in range(k) ]
```
