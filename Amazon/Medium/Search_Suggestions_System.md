# [Home](./../..)/[Amazon](./..)/[Medium](./)/Search_Suggestions_System
<h1>Search Suggestions System</h1>

<p>
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
</p>
<p>
Return list of lists of the suggested products after each character of searchWord is typed. 
</p>

<b>Example 1:</b>

    Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
    Output: [
    ["mobile","moneypot","monitor"],
    ["mobile","moneypot","monitor"],
    ["mouse","mousepad"],
    ["mouse","mousepad"],
    ["mouse","mousepad"]
    ]
    Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
    After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
    After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
    
<b>Example 2:</b>

    Input: products = ["havana"], searchWord = "havana"
    Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
    
<b>Example 3:</b>

    Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
    Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

<b>Constraints:</b>

- 1 <= products.length <= 1000
- There are no repeated elements in products.
- 1 <= Σ products[i].length <= 2 * 10^4
- All characters of products[i] are lower-case English letters.
- 1 <= searchWord.length <= 1000
- All characters of searchWord are lower-case English letters.

<h2>Solution</h2>

```python
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        search = ''
        idx = 0
        ans = []
        for c in searchWord:
            search += c
            idx = bisect.bisect_left(products, search)
            t = []
            for word in products[idx: idx+3]:
                if word.startswith(search):
                    t.append(word)
            ans.append(t)
        return ans
```
