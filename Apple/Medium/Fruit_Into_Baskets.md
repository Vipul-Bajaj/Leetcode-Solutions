# [Home](./../..)/[Apple](./..)/[Medium](./)/Fruit_Into_Baskets
<h1>Fruit Into Baskets</h1>

<p>
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
</p>
<p>
You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
</p>
  
* You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
* Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
* Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

<p>
Given the integer array fruits, return the maximum number of fruits you can pick.
</p>

<b>Example 1:</b>

    Input: fruits = [1,2,1]
    Output: 3
    Explanation: We can pick from all 3 trees.
    
<b>Example 2:</b>

    Input: fruits = [0,1,2,2]
    Output: 3
    Explanation: We can pick from trees [1,2,2].
    If we had started at the first tree, we would only pick from trees [0,1].
    
<b>Example 3:</b>

    Input: fruits = [1,2,3,2,2]
    Output: 4
    Explanation: We can pick from trees [2,3,2,2].
    If we had started at the first tree, we would only pick from trees [1,2].
    
<b>Example 4:</b>

    Input: fruits = [3,3,3,1,2,1,1,2,3,3,4]
    Output: 5
    Explanation: We can pick from trees [1,2,1,1,2].

<b>Constraints:</b>

- 1 <= nums.length <= 15
- -100 <= nums[i] <= 100

<h2>Solution</h2>

```python
# # With Two loop
# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         ans = 0
#         n = len(fruits)
#         f = 0
#         l = None
#         i = 1
#         while i<n:
#             fruit = fruits[i]
#             if fruit != fruits[f] and not l:
#                 l = i
#             if fruit != fruits[f] and fruit != fruits[l]:
#                 ans = max(ans,i-f)
#                 f = i-1
#                 while fruits[f-1] == fruits[i-1]:
#                     f-=1
#                 l = i
#             i+=1
#         ans = max(ans,i-f)
#         return ans
# With one loop    
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        first,second = -1,-1
        count = 0
        ans = 0
        temp = 0
        for fruit in fruits:
            if second == -1:
                second = fruit
                temp = 1
            elif fruit != second and first == -1:
                second,first = fruit,second
                temp = 1
            elif fruit == second:
                temp+=1
            elif fruit == first:
                second,first = first,second
                temp = 1
            else:
                second,first = fruit,second
                ans = max(ans,count)
                count,temp = temp,1
            count+=1
        return max(count,ans)
```
