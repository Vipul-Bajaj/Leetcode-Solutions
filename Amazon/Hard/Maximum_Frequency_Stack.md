# [Home](./../..)/[Amazon](./..)/[Hard](./)/Maximum_Frequency_Stack
<h1>Maximum Frequency Stack</h1>

<p>
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:
</p>

- FreqStack() constructs an empty frequency stack.
- void push(int val) pushes an integer val onto the top of the stack.
- int pop() removes and returns the most frequent element in the stack.

<p>
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
</p>

<b>Example 1:</b>

    Input
    ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
    [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
    Output
    [null, null, null, null, null, null, null, 5, 7, 5, 4]

    Explanation
    FreqStack freqStack = new FreqStack();
    freqStack.push(5); // The stack is [5]
    freqStack.push(7); // The stack is [5,7]
    freqStack.push(5); // The stack is [5,7,5]
    freqStack.push(7); // The stack is [5,7,5,7]
    freqStack.push(4); // The stack is [5,7,5,7,4]
    freqStack.push(5); // The stack is [5,7,5,7,4,5]
    freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
    freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
    freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
    freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].

<b>Constraints:</b>

- 0 <= val <= 109
- At most 2 * 104 calls will be made to push and pop.
- It is guaranteed that there will be at least one element in the stack before calling pop

<h2>Solution</h2>

```python
class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.freq_group = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = self.freq[val] + 1
        self.freq[val] = freq
        if freq>self.max_freq:
            self.max_freq = freq
        self.freq_group[freq].append(val)

    def pop(self) -> int:
        x = self.freq_group[self.max_freq].pop()
        self.freq[x]-=1
        if not self.freq_group[self.max_freq]:
            self.max_freq-=1
        return x
            


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
```
