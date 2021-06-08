# [Home](./../..)/[Expedia](./..)/[Medium](./)/Reconstruct_Original_Digits_from_English
<h1>Reconstruct Original Digits from English</h1>

<p>
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.
</p>

<b>Example 1:</b>

    Input: s = "owoztneoer"
    Output: "012"
    
<b>Example 2:</b>

    Input: s = "fviefuro"
    Output: "45"

<b>Constraints:</b>

- 1 <= s.length <= 105
- s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
- s is guaranteed to be valid.

<h2>Solution</h2>

```python
class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        arr = [0]*10
        arr[0] = count['z']
        arr[2] = count['w']
        arr[4] = count['u']
        arr[6] = count['x']
        arr[8] = count['g']
        arr[3] = count['h']-arr[8]
        arr[5] = count['f']-arr[4]
        arr[7] = count['s']-arr[6]
        arr[9] = count['i']-arr[5]-arr[6]-arr[8]
        arr[1] = count['n']-arr[7]-2*arr[9]
        
        output = [str(i)*x for i,x in enumerate(arr)]
        return "".join(output)
```
