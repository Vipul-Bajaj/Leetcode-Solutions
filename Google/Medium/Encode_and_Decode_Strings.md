# [Home](./../..)/[Google](./..)/[Medium](./)/Encode_and_Decode_Strings
<h1>Encode and Decode Strings</h1>

<p>
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
</p>
<p>
Machine 1 (sender) has the function:
</p>

    string encode(vector<string> strs) {
      // ... your code
      return encoded_string;
    }

<p>
Machine 2 (receiver) has the function:
</p>

    vector<string> decode(string s) {
      //... your code
      return strs;
    }

<p>    
So Machine 1 does:
</p>
    
    string encoded_string = encode(strs);
<p>
and Machine 2 does:
</p>

    vector<string> strs2 = decode(encoded_string);
    
<p>    
strs2 in Machine 2 should be the same as strs in Machine 1.
</p>
<p>
Implement the encode and decode methods.
</p>
<p>
You are not allowed to solve the problem using any serialize methods (such as eval).
</p>

<b>Example 1:</b>

    Input: dummy_input = ["Hello","World"]
    Output: ["Hello","World"]
    Explanation:
    Machine 1:
    Codec encoder = new Codec();
    String msg = encoder.encode(strs);
    Machine 1 ---msg---> Machine 2

    Machine 2:
    Codec decoder = new Codec();
    String[] strs = decoder.decode(msg);
    
<b>Example 2:</b>    

    Input: dummy_input = [""]
    Output: [""]

<b>Constraints:</b>

- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] contains any possible characters out of 256 valid ASCII characters.

<h2>Solution</h2>

```python
class Codec:
    def len_to_bytes_str(self,n):
        bytes_str = [chr(n>>(i*8)&0xff) for i in range(4)]
        bytes_str.reverse()
        return "".join(bytes_str)
    
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "".join(self.len_to_bytes_str(len(s))+s for s in strs)   

    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result
    
    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_int(s[i: i + 4])
            i += 4
            output.append(s[i: i + length])
            i += length
        return output


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
```
