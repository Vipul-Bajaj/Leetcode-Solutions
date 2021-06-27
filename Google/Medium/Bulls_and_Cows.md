# [Home](./../..)/[Google](./..)/[Medium](./)/Bulls_and_Cows
<h1>Bulls and Cows</h1>

<p>
You are playing the Bulls and Cows game with your friend.
<br>
You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:
</p>

* The number of "bulls", which are digits in the guess that are in the correct position.
* The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.

<p>
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.
<br>
The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.
</p>

<b>Example 1:</b>

    Input: secret = "1807", guess = "7810"
    Output: "1A3B"
    Explanation: Bulls are connected with a '|' and cows are underlined:
    "1807"
      |
    "7810"
    
<b>Example 2:</b>    

    Input: secret = "1123", guess = "0111"
    Output: "1A1B"
    Explanation: Bulls are connected with a '|' and cows are underlined:
    "1123"        "1123"
      |      or     |
    "0111"        "0111"
    Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
    
<b>Example 3:</b>     

    Input: secret = "1", guess = "0"
    Output: "0A0B"
    
<b>Example 4:</b>       

    Input: secret = "1", guess = "1"
    Output: "1A0B"

<b>Constraints:</b>

- 1 <= secret.length, guess.length <= 1000
- secret.length == guess.length
- secret and guess consist of digits only.

<h2>Solution</h2>

```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hm = Counter(secret)
        b,c= 0,0
        for i,ch in enumerate(guess):
            if ch in hm:
                if ch == secret[i]:
                    b+=1
                    c-=int(hm[ch]<=0)
                else:
                    c+=int(hm[ch]>0)
                hm[ch]-=1
        return "{}A{}B".format(b,c)
```
