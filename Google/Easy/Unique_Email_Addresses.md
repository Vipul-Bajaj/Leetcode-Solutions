# [Home](./../..)/[Google](./..)/[Easy](./)/Unique_Email_Addresses
<h1>Unique Email Addresses</h1>

<p>
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
</p>

* For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.

<p>
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
</p>

* For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.

<p>
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.
</p>

* For example, "m.y+name@email.com" will be forwarded to "my@email.com".

<p>
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each email[i], return the number of different addresses that actually receive mails.
</p>

<b>Example 1:</b>

    Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    Output: 2
    Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
    
<b>Example 2:</b>

    Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    Output: 3

<b>Constraints:</b>

- 1 <= emails.length <= 100
- 1 <= emails[i].length <= 100
- email[i] consist of lowercase English letters, '+', '.' and '@'.
- Each emails[i] contains exactly one '@' character.
- All local and domain names are non-empty.
- Local names do not start with a '+' character.

<h2>Solution</h2>

```python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for idx, email in enumerate(emails):
            e = email.split('@')[0].replace('.', '').split('+')[0]
            emails[idx] = e + '@' + email.split('@')[1]
        return len(set(emails))
```
