# [Home](./../../..)/[Intuit](./../..)/[Hard](./..)/Text_Justification
# [Home](./../../..)/[Intuit](./../..)/[Hard](./..)/Text_Justification
<h1>Text Justification</h1>

<p>
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

- A word is defined as a character sequence consisting of non-space characters only.
- Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
- The input array words contains at least one word.

</p>

<b>Example 1:</b>

    Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
    Output:
    [
       "This    is    an",
       "example  of text",
       "justification.  "
    ]
    
<b>Example 2:</b>

    Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
    Output:
    [
      "What   must   be",
      "acknowledgment  ",
      "shall be        "
    ]
    Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
    Note that the second line is also left-justified becase it contains only one word.
    
<b>Example 3:</b>

    Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
    Output:
    [
      "Science  is  what we",
      "understand      well",
      "enough to explain to",
      "a  computer.  Art is",
      "everything  else  we",
      "do                  "
    ]

<b>Constraints:</b>

- 1 <= words.length <= 300
- 1 <= words[i].length <= 20
- words[i] consists of only English letters and symbols.
- 1 <= maxWidth <= 100
- words[i].length <= maxWidth

<h2>Solution</h2>

```python
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        line = ""
        for word in words:
            if len(line + word)<=maxWidth:
                line += word + " "
            else:
                lines.append(line.strip())
                line = word + " "
        line = line.strip()
        spaces = maxWidth-len(line)
        lines.append(line + " "*spaces)
        # print(lines)
        n = len(lines)
        for i in range(n-1):
            words = lines[i].split(" ")
            spaces = len(words)-1
            spaces_needed = maxWidth-len(lines[i])+spaces
            line = ""
            if len(words) ==1:
                line = words[0] + " "*(maxWidth-len(words[0]))
            else:
                for word in words:
                    space = 0
                    if spaces_needed > 0 and spaces >0:
                        space = ceil(spaces_needed/spaces)
                        spaces_needed-=space
                        spaces-=1
                    line += word + " "*space
            lines[i] = line
        # for line in lines:
        #     print(len(line))
        return lines
```
