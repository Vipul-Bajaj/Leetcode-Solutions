# [Home](./../..)/[Amazon](./..)/[Easy](./)/Reorder_Data_in_Log_Files
<h1>Reorder Data in Log Files</h1>

<p>
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

1. The letter-logs come before all digit-logs.
2. The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
3. The digit-logs maintain their relative ordering.

Return the final order of the logs.

</p>

<b>Example 1:</b>

    Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    Explanation:
    The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
    The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
    
<b>Example 2:</b>

    Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
 
<b>Constraints:</b>

- 1 <= logs.length <= 100
- 3 <= logs[i].length <= 100
- All the tokens of logs[i] are separated by a single space.
- logs[i] is guaranteed to have an identifier and at least one word after the identifier.

<h2>Solution</h2>

```python
# class Solution:
#     def _isDigiLog(self,s:str):
#         if s.isdigit():
#             return True
#         return False
    
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         digi_logs = []
#         letter_logs = []
#         for log in logs:
#             log = log.split()
#             if self._isDigiLog(log[1]):
#                 digi_logs.append(" ".join(log))
#             else:
#                 letter_logs.append(" ".join(log))
                
#         new_letter_logs = []
#         for x in letter_logs:
#             x = x.split()
#             new_letter_logs.append((x[0]," ".join(x[1:])))
                
#         letter_logs = sorted(new_letter_logs,key=lambda x:(x[1],x[0]))
#         letter_logs = [" ".join(x) for x in letter_logs]
#         return letter_logs + digi_logs

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)
```
