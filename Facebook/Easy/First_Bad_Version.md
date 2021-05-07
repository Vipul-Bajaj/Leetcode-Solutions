# [Home](./../..)/[Facebook](./..)/[Easy](./)/First_Bad_Version
<h1>First Bad Version</h1>

<p>
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
</p>

<b>Example 1:</b>

    Input: n = 5, bad = 4
    Output: 4
    Explanation:
    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true
    Then 4 is the first bad version.
    
<b>Example 2:</b>

    Input: n = 1, bad = 1
    Output: 1

<b>Constraints:</b>

- 1 <= bad <= n <= 231 - 1

<h2>Solution</h2>

```python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low<=high:
            mid = (low+high)//2
            isBad = isBadVersion(mid)
            isPrevBad  = isBadVersion(mid-1)
            if isBad and not isPrevBad:
                return mid
            elif not isBad:
                low = mid+1
            else:
                high = mid
```
