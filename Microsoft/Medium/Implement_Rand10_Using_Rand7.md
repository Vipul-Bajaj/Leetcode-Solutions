# [Home](./../..)/[Microsoft](./..)/[Medium](./)/Implement_Rand10_Using_Rand7
<h1>Implement Rand10() Using Rand7()</h1>

<p>
Given the API rand7() that generates a uniform random integer in the range [1, 7], write a function rand10() that generates a uniform random integer in the range [1, 10]. You can only call the API rand7(), and you shouldn't call any other API. Please do not use a language's built-in random API.
</p>
<p>
Each test case will have one internal argument n, the number of times that your implemented function rand10() will be called while testing. Note that this is not an argument passed to rand10().
</p>
<p>
Follow up:
</p>

* What is the expected value for the number of calls to rand7() function?
* Could you minimize the number of calls to rand7()?
</p>

<b>Example 1:</b>

    Input: n = 1
    Output: [2]

<b>Example 2:</b>

    Input: n = 2
    Output: [2,8]

<b>Example 3:</b>

    Input: n = 3
    Output: [3,8,10]

<b>Constraints:</b>

- 1 <= n <= 10^5

<h2>Solution</h2>

```python
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row = rand7()
            col = rand7()
            idx = col+(row-1)*7
            if idx<=40:
                break
        return 1 + (idx-1)%10
```
