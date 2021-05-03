# [Home](./../../..)/[Facebook](./../..)/[Medium](./..)/Accounts_Merge
<h1>Accounts Merge</h1>

<p>
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

</p>

<b>Example 1:</b>

    Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    Explanation:
    The first and third John's are the same person as they have the common email "johnsmith@mail.com".
    The second John and Mary are different people as none of their email addresses are used by other accounts.
    We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
    ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
    
<b>Example 2:</b>

    Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
    Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

<b>Constraints:</b>

- 1 <= accounts.length <= 1000
- 2 <= accounts[i].length <= 10
- 1 <= accounts[i][j] <= 30
- accounts[i][0] consists of English letters.
- accounts[i][j] (for j > 0) is a valid email.

<h2>Solution</h2>

```python
class Solution:
    def dfs(self,node,emails_graph,res):
        self.visited.add(node)
        res.add(node)
        for email in emails_graph[node]:
            if email not in self.visited:
                res.add(email)
                self.dfs(email,emails_graph,res)
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails_graph = defaultdict(list)
        email_association = {}
        
        for account in accounts:
            emails = account[1:]
            node_email = emails[0]
            email_association[node_email] = account[0]
            if len(emails)>1:
                for email in emails[1:]:
                    emails_graph[node_email].append(email)
                    emails_graph[email].append(node_email)
                    email_association[email] = account[0]
            else:
                emails_graph[node_email] = []
        
        # print(emails_graph)
        self.visited = set()
        ans = []
        for email in emails_graph.keys():
            account = set()
            if email not in self.visited:
                self.dfs(email,emails_graph,account)
                res = [email_association[email]] + sorted(account)
                ans.append(res)
                
        return ans
```
