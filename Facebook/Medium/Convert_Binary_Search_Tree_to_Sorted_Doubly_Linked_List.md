# [Home](./../..)/[Facebook](./..)/[Medium](./)/Convert_Binary_Search_Tree_to_Sorted_Doubly_Linked_List
<h1>Convert Binary Search Tree to Sorted Doubly Linked List</h1>

<p>
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
</p>
<p>  
You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
</p>
<p>
We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.
</p>

<b>Example 1:</b>

<img src="https://assets.leetcode.com/uploads/2018/10/12/bstdlloriginalbst.png">

    Input: root = [4,2,5,1,3]
    
<img src="https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png">

    Output: [1,2,3,4,5]
    Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.
<img src="https://assets.leetcode.com/uploads/2018/10/12/bstdllreturnbst.png">    

<b>Example 2:</b>

    Input: root = [2,1,3]
    Output: [1,2,3]

<b>Example 3:</b>

    Input: root = []
    Output: []
    Explanation: Input is an empty tree. Output is also an empty Linked List.

<b>Example 4:</b>

    Input: root = [1]
    Output: [1]

<b>Constraints:</b>

- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000
- All the values of the tree are unique.

<h2>Solution</h2>

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
# Iterative method using extra space
# class Solution:
#     def treeToDoublyList(self, root: 'Node') -> 'Node':
#         st = []
#         arr = []
#         while True:
#             if root:
#                 st.append(root)
#                 root = root.left
#             elif st:
#                 root = st.pop()
#                 arr.append(root)
#                 root = root.right
#             else:
#                 break
#         for i,ele in enumerate(arr):
#             ele.left = arr[i-1]
#             ele.right = arr[(i+1)%len(arr)]
#         return arr[0] if arr else root

# Recurssive method
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            """
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            """
            nonlocal last, first
            if node:
                # left
                helper(node.left)
                # node 
                if last:
                    # link the previous node (last)
                    # with the current one (node)
                    last.right = node
                    node.left = last
                else:
                    # keep the smallest node
                    # to close DLL later on
                    first = node        
                last = node
                # right
                helper(node.right)
        
        if not root:
            return None
        
        # the smallest (first) and the largest (last) nodes
        first, last = None, None
        helper(root)
        # close DLL
        last.right = first
        first.left = last
        return first
```
