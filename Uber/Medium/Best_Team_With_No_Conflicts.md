# [Home](./../..)/[Uber](./..)/[Medium](./)/Best_Team_With_No_Conflicts
<h1>Best Team With No Conflicts</h1>

<p>
You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.
</p>
<p>
However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.
</p>
<p>
Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.
</p>

<b>Example 1:</b>

    Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
    Output: 34
    Explanation: You can choose all the players.

<b>Example 2:</b>

    Input: scores = [4,5,6,5], ages = [2,1,2,1]
    Output: 16
    Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.

<b>Example 3:</b>

    Input: scores = [1,2,3,5], ages = [8,9,10,1]
    Output: 6
    Explanation: It is best to choose the first 3 players. 
<b>Constraints:</b>

- 1 <= scores.length, ages.length <= 1000
- scores.length == ages.length
- 1 <= scores[i] <= 106
- 1 <= ages[i] <= 1000

<h2>Solution</h2>

```python
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        max_scores=[0]*(max(ages)+1)
        
        for score, age in sorted(zip(scores, ages)): 
            max_scores[age] = score + max(max_scores[:age + 1])

        return max(max_scores)
```
