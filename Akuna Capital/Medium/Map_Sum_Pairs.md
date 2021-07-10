# [Home](./../..)/[Akuna Capital](./..)/[Medium](./)/Map_Sum_Pairs
<h1>Map Sum Pairs</h1>

<p>
Implement the MapSum class:
</p>

* MapSum() Initializes the MapSum object.
* void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
* int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.

<b>Example 1:</b>

    Input
    ["MapSum", "insert", "sum", "insert", "sum"]
    [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
    Output
    [null, null, 3, null, 5]

    Explanation
    MapSum mapSum = new MapSum();
    mapSum.insert("apple", 3);  
    mapSum.sum("ap");           // return 3 (apple = 3)
    mapSum.insert("app", 2);    
    mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)

<b>Constraints:</b>

- 1 <= key.length, prefix.length <= 50
- key and prefix consist of only lowercase English letters.
- 1 <= val <= 1000
- At most 50 calls will be made to insert and sum.

<h2>Solution</h2>

```python
class TrieNode(object):
    __slots__ = 'children', 'score'
    def __init__(self):
        self.children = {}
        self.score = 0
        
    def __repr__(self):
        return repr("[" + ','.join(self.children.values()) +"], score: " + str(self.score))
        
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.hm = {}
        
    def insert(self, key: str, val: int) -> None:
        adj = val-self.hm.get(key,0)
        self.hm[key] = val
        curr = self.root
        curr.score+=adj
        for ch in key:
            curr = curr.children.setdefault(ch,TrieNode())
            curr.score+=adj
        
    def sum(self, prefix: str) -> int:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]
        return curr.score
            


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
```
