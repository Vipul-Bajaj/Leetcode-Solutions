# [Home](./../..)/[Yelp](./..)/[Easy](./)/Minimum_Index_Sum_of_Two_Lists
<h1>Minimum Index Sum of Two Lists</h1>

<p>
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
</p>
<p>
You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
</p>

<b>Example 1:</b>

    Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    Output: ["Shogun"]
    Explanation: The only restaurant they both like is "Shogun".
    
<b>Example 2:</b>

    Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
    Output: ["Shogun"]
    Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
    
<b>Example 3:</b>

    Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
    Output: ["KFC","Burger King","Tapioca Express","Shogun"]

<b>Constraints:</b>

- 1 <= list1.length, list2.length <= 1000
- 1 <= list1[i].length, list2[i].length <= 30
- list1[i] and list2[i] consist of spaces ' ' and English letters.
- All the stings of list1 are unique.
- All the stings of list2 are unique.
<h2>Solution</h2>

```python
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hm = {}
        min_idx = float('inf')
        out = []
        for idx,item in enumerate(list1):
            hm[item] = idx
        for idx,item in enumerate(list2):
            if item in hm:
                s = idx+hm[item]
                if s<min_idx:
                    out = []
                    min_idx = s
                    out.append(item)
                elif s == min_idx:
                    out.append(item)
        return out
```
