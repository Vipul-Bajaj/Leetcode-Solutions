# [Home](./../..)/[Facebook](./..)/[Hard](./)/Valid_Number
<h1>Valid Number</h1>

<p>
A valid number can be split up into these components (in order):
</p>

* A decimal number or an integer.
* (Optional) An 'e' or 'E', followed by an integer.

<p>
A decimal number can be split up into these components (in order):
</p>

* (Optional) A sign character (either '+' or '-').
* One of the following formats:
    * At least one digit, followed by a dot '.'.
    * At least one digit, followed by a dot '.', followed by at least one digit.
    * A dot '.', followed by at least one digit.

<p>
An integer can be split up into these components (in order):
</p>

* (Optional) A sign character (either '+' or '-').
* At least one digit.

<p> 
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.
</p>

<b>Example 1:</b>

    Input: s = "0"
    Output: true
    
<b>Example 2:</b>

    Input: s = "e"
    Output: false

<b>Example 3:</b>

    Input: s = "."
    Output: false
    
<b>Example 4:</b>

    Input: s = ".1"
    Output: true
    
<b>Constraints:</b>

- 1 <= s.length <= 20
- s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.

<h2>Solution</h2>

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_exponent = seen_dot =  False
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ["+", "-"]:
                if i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
            elif c in ["e", "E"]:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif c == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False
        
        return seen_digit
```
