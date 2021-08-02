# [Home](./../..)/[Google](./..)/[Medium](./)/Evaluate_the_Bracket_Pairs_of_a_String
<h1>Evaluate the Bracket Pairs of a String</h1>

<p>
You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.
</p>

- For example, in the string "(name)is(age)yearsold", there are two bracket pairs that contain the keys "name" and "age".

<p>
You know the values of a wide range of keys. This is represented by a 2D string array knowledge where each knowledge[i] = [keyi, valuei] indicates that key keyi has a value of valuei.
</p>
<p>
You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair that contains some key keyi, you will:
</p>

- Replace keyi and the bracket pair with the key's corresponding valuei.
- If you do not know the value of the key, you will replace keyi and the bracket pair with a question mark "?" (without the quotation marks).

<p>
Each key will appear at most once in your knowledge. There will not be any nested brackets in s.
<br>
Return the resulting string after evaluating all of the bracket pairs.
</p>

<b>Example 1:</b>

    Input: s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
    Output: "bobistwoyearsold"
    Explanation:
    The key "name" has a value of "bob", so replace "(name)" with "bob".
    The key "age" has a value of "two", so replace "(age)" with "two".

<b>Example 2:</b>    

    Input: s = "hi(name)", knowledge = [["a","b"]]
    Output: "hi?"
    Explanation: As you do not know the value of the key "name", replace "(name)" with "?".

<b>Example 3:</b>    

    Input: s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]
    Output: "yesyesyesaaa"
    Explanation: The same key can appear multiple times.
    The key "a" has a value of "yes", so replace all occurrences of "(a)" with "yes".
    Notice that the "a"s not in a bracket pair are not evaluated.

<b>Example 4:</b>    

    Input: s = "(a)(b)", knowledge = [["a","b"],["b","a"]]
    Output: "ba"

<b>Constraints:</b>

- 1 <= s.length <= 105
- 0 <= knowledge.length <= 105
- knowledge[i].length == 2
- 1 <= keyi.length, valuei.length <= 10
- s consists of lowercase English letters and round brackets '(' and ')'.
- Every open bracket '(' in s will have a corresponding close bracket ')'.
- The key in each bracket pair of s will be non-empty.
- There will not be any nested bracket pairs in s.
- keyi and valuei consist of lowercase English letters.
- Each keyi in knowledge is unique.

<h2>Solution</h2>

```python
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {k:v for k, v in knowledge}
        t = s.split("(")
        ans = t[0]
        for i in range(1, len(t)):
            a, b = t[i].split(")")
            ans += d.get(a, "?") + b
        return ans
```
