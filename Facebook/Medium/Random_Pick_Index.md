# [Home](./../..)/[Facebook](./..)/[Medium](./)/Random_Pick_Index
<h1>Random Pick Index</h1>

<p>
Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
</p>
<p>
Implement the Solution class:
</p>

- Solution(int[] nums) Initializes the object with the array nums.
- int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.

<b>Example 1:</b>

    Input
    ["Solution", "pick", "pick", "pick"]
    [[[1, 2, 3, 3, 3]], [3], [1], [3]]
    Output
    [null, 4, 0, 2]

    Explanation
    Solution solution = new Solution([1, 2, 3, 3, 3]);
    solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
    solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
    solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.

<b>Constraints:</b>

- 1 <= nums.length <= 2 * 104
- -231 <= nums[i] <= 231 - 1
- target is an integer from nums.
- At most 104 calls will be made to pick.

<h2>Solution</h2>

```python
class Solution:

    def __init__(self, nums: List[int]):
        self.hm = {}
        for idx,n in enumerate(nums):
            if n in self.hm:
                self.hm[n].append(idx)
            else:
                self.hm[n] = [idx]
        

    def pick(self, target: int) -> int:
        return random.choice(self.hm[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
```
