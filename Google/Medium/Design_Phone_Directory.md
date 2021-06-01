# [Home](./../..)/[Google](./..)/[Medium](./)/Design_Phone_Directory
<h1>Design Phone Directory</h1>

<p>
Design a phone directory that initially has maxNumbers empty slots that can store numbers. The directory should store numbers, check if a certain slot is empty or not, and empty a given slot.
<br>
Implement the PhoneDirectory class:
</p>

* PhoneDirectory(int maxNumbers) Initializes the phone directory with the number of available slots maxNumbers.
* int get() Provides a number that is not assigned to anyone. Returns -1 if no number is available.
* bool check(int number) Returns true if the slot number is available and false otherwise.
* void release(int number) Recycles or releases the slot number.

<b>Example 1:</b>

    Input: root = [1,2,3], fromNode = 2, toNode = 3
    ["PhoneDirectory", "get", "get", "check", "get", "check", "release", "check"]
    [[3], [], [], [2], [], [2], [2], [2]]
    Output
    [null, 0, 1, true, 2, false, null, true]

    Explanation
    PhoneDirectory phoneDirectory = new PhoneDirectory(3);
    phoneDirectory.get();      // It can return any available phone number. Here we assume it returns 0.
    phoneDirectory.get();      // Assume it returns 1.
    phoneDirectory.check(2);   // The number 2 is available, so return true.
    phoneDirectory.get();      // It returns 2, the only number that is left.
    phoneDirectory.check(2);   // The number 2 is no longer available, so return false.
    phoneDirectory.release(2); // Release number 2 back to the pool.
    phoneDirectory.check(2);   // Number 2 is available again, return true.

<b>Constraints:</b>

- 1 <= maxNumbers <= 104
- 0 <= number < maxNumbers
- At most 2 * 104 calls will be made to get, check, and release.

<h2>Solution</h2>

```python
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.free = set(range(maxNumbers))

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        return self.free.pop() if self.free else -1

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return number in self.free

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        self.free.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
```
