<h1>Count and Say</h1>

<p>
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
</p>

* countAndSay(1) = "1"
* countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

<p>
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251":

<img src="https://assets.leetcode.com/uploads/2020/10/23/countandsay.jpg">
</p>

<p>
Given a positive integer n, return the nth term of the count-and-say sequence.

</p>

<b>Example 1:</b>

    Input: n = 1
    Output: "1"
    Explanation: This is the base case.
    
<b>Example 2:</b>

    Input: n = 4
    Output: "1211"
    Explanation:
    countAndSay(1) = "1"
    countAndSay(2) = say "1" = one 1 = "11"
    countAndSay(3) = say "11" = two 1's = "21"
    countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

<b>Constraints:</b>

- 1 <= n <= 30

<h2>Solution</h2>

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        ans = ['1']
        i = 2
        while i <= n:
            temp = int("".join(ans[::-1]))
            ans = []
            last = None
            count = 0
            while temp:
                r = temp%10
                temp = temp//10
                if not last:
                    last = r
                    count = 1
                elif r == last:
                    count+=1
                else:
                    ans.append(str(count))
                    ans.append(str(last))
                    last = r
                    count = 1
            ans.append(str(count))
            ans.append(str(last))
            i+=1
        return "".join(ans)
```
