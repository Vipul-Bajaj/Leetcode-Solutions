# [Home](./../..)/[Google](./..)/[Medium](./)/Maximum_Font_to_Fit_a_Sentence_in_a_Screen
<h1>Maximum Font to Fit a Sentence in a Screen</h1>

<p>
You are given a string text. We want to display text on a screen of width w and height h. You can choose any font size from array fonts, which contains the available font sizes in ascending order.
</p>
<p>
You can use the FontInfo interface to get the width and height of any character at any available font size.
</p>
<p>
The FontInfo interface is defined as such:
</p>

    interface FontInfo {
      // Returns the width of character ch on the screen using font size fontSize.
      // O(1) per call
      public int getWidth(int fontSize, char ch);

      // Returns the height of any character on the screen using font size fontSize.
      // O(1) per call
      public int getHeight(int fontSize);
    }

<p>    
The calculated width of text for some fontSize is the sum of every getWidth(fontSize, text[i]) call for each 0 <= i < text.length (0-indexed). The calculated height of text for some fontSize is getHeight(fontSize). Note that text is displayed on a single line.
</p>
<p>
It is guaranteed that FontInfo will return the same value if you call getHeight or getWidth with the same parameters.
</p>
<p>
It is also guaranteed that for any font size fontSize and any character ch:
</p>

- getHeight(fontSize) <= getHeight(fontSize+1)
- getWidth(fontSize, ch) <= getWidth(fontSize+1, ch)

<p>
Return the maximum font size you can use to display text on the screen. If text cannot fit on the display with any font size, return -1.
</p>

<b>Example 1:</b>

    Input: text = "helloworld", w = 80, h = 20, fonts = [6,8,10,12,14,16,18,24,36]
    Output: 6

<b>Example 2:</b>

    Input: text = "leetcode", w = 1000, h = 50, fonts = [1,2,4]
    Output: 4

<b>Example 3:</b>

    Input: text = "easyquestion", w = 100, h = 100, fonts = [10,15,20,25]
    Output: -1
    
<b>Constraints:</b>

- 1 <= text.length <= 50000
- text contains only lowercase English letters.
- 1 <= w <= 107
- 1 <= h <= 104
- 1 <= fonts.length <= 105
- 1 <= fonts[i] <= 105
- fonts is sorted in ascending order and does not contain duplicates.

<h2>Solution</h2>

```python
# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        def getTotalWidthHeight(font):
            tw = 0
            for ch in text:
                tw+=fontInfo.getWidth(font,ch)
            return tw,fontInfo.getHeight(font)
        l = 0
        r = len(fonts)-1
        ans = -1
        while l<=r:
            m = (l+r)//2
            tw,th = getTotalWidthHeight(fonts[m])
            if (tw==w and th<=h) or (tw<=w and th==h):
                return fonts[m]
            if tw>w or th>h:
                r = m-1
            else:
                ans = max(ans,fonts[m])
                l = m+1
        return ans
```
