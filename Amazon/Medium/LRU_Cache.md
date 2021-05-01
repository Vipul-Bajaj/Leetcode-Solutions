<h1>LRU Cache</h1>

<p>
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

<b>Follow up:</b>
Could you do get and put in O(1) time complexity?

</p>

<b>Example 1:</b>

    Input
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    Output
    [null, null, null, 1, null, -1, null, -1, 3, 4]

    Explanation
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1); // cache is {1=1}
    lRUCache.put(2, 2); // cache is {1=1, 2=2}
    lRUCache.get(1);    // return 1
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.get(2);    // returns -1 (not found)
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1);    // return -1 (not found)
    lRUCache.get(3);    // return 3
    lRUCache.get(4);    // return 4
 
<b>Constraints:</b>

    1 <= capacity <= 3000
    0 <= key <= 3000
    0 <= value <= 104
    At most 3 * 104 calls will be made to get and put.

<h2>Solution</h2>

```python
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.hash_map = {}
#         self.lru = []
#         self.capacity = capacity
#         self.filled = 0

#     def get(self, key: int) -> int:
#         if key in self.hash_map:
#             self.lru.remove(key)
#             self.lru.append(key)
#             return self.hash_map[key]
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.hash_map:
#             self.lru.remove(key)
#             self.lru.append(key)
#             self.hash_map[key]=value
#         else:
#             if self.filled>=self.capacity:
#                 ele = self.lru.pop(0)
#                 del self.hash_map[ele]
#             else:
#                 self.filled+=1
#             self.hash_map[key]=value
#             self.lru.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Solution Implementation
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.dict = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        self.dict.move_to_end(key)
        return self.dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.move_to_end(key)
        self.dict[key]=value
        if len(self.dict)>self.capacity:
            self.dict.popitem(last=False)
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```
