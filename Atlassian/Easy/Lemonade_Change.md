# [Home](./../..)/[Atlassian](./..)/[Easy](./)/Lemonade_Change
<h1>Lemonade Change</h1>

<p>
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
</p>
<p>
Note that you don't have any change in hand at first.
</p>
<p>
Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with correct change, or false otherwise.
</p>

<b>Example 1:</b>

    Input: bills = [5,5,5,10,20]
    Output: true
    Explanation: 
    From the first 3 customers, we collect three $5 bills in order.
    From the fourth customer, we collect a $10 bill and give back a $5.
    From the fifth customer, we give a $10 bill and a $5 bill.
    Since all customers got correct change, we output true.

<b>Example 2:</b>

    Input: bills = [5,5,10,10,20]
    Output: false
    Explanation: 
    From the first two customers in order, we collect two $5 bills.
    For the next two customers in order, we collect a $10 bill and give back a $5 bill.
    For the last customer, we can not give change of $15 back because we only have two $10 bills.
    Since not every customer received correct change, the answer is false.

<b>Example 3:</b>

    Input: bills = [5,5,10]
    Output: true

<b>Example 4:</b>

    Input: bills = [10,10]
    Output: false

<b>Constraints:</b>

- 1 <= bills.length <= 105
- bills[i] is either 5, 10, or 20.

<h2>Solution</h2>

```python
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hm = {5:0,10:0,20:0}
        for bill in bills:
            if bill == 5:
                hm[bill]+=1
                continue
            if bill == 10:
                if hm[5]<1:
                    return False
                hm[bill]+=1
                hm[5]-=1
                continue
            if bill == 20:
                if hm[10]>0 and hm[5]>0:
                    hm[10]-=1
                    hm[5]-=1
                    hm[bill]+=1
                elif hm[5]>2:
                    hm[5]-=3
                    hm[bill]+=1
                else:
                    return False
        return True
```
