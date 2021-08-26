# [Home](./../..)/[Google](./..)/[Medium](./)/Verify_Preorder_Serialization_of_a_Binary_Tree
<h1>Verify Preorder Serialization of a Binary Tree
</h1>

<p>
One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'.
</p>
<p>
<img src="https://assets.leetcode.com/uploads/2021/03/12/pre-tree.jpg">

For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.
</p>
<p>
Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.
</p>
<p>
It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.
</p>
<p>
You may assume that the input format is always valid.
</p>

- For example, it could never contain two consecutive commas, such as "1,,3".

<p>
Note: You are not allowed to reconstruct the tree.
</p>

<b>Example 1:</b>

    Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    Output: true

<b>Example 2:</b>

    Input: preorder = "1,#"
    Output: false

<b>Example 3:</b>

    Input: preorder = "9,#,#,1"
    Output: false
    
<b>Constraints:</b>

- 1 <= preorder.length <= 104
- preoder consist of integers in the range [0, 100] and '#' separated by commas ','.

<h2>Solution</h2>

```python
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        prev = None
        for ch in preorder:
            if ch == ',':
                slots-=1
                if slots<0:
                    return False
                if prev != '#':
                    slots+=2
            prev = ch
        slots = slots+1 if ch != '#' else slots-1
        return slots == 0
```
