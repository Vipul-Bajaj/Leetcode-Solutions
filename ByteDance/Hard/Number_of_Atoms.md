<h1>Number of Atoms</h1>

<p>
Given a chemical formula (given as a string), return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together to produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

<b>Example 1:</b>

    Input: formula = "H2O"
    Output: "H2O"
    Explanation: The count of elements are {'H': 2, 'O': 1}.
    
<b>Example 2:</b>

    Input: formula = "Mg(OH)2"
    Output: "H2MgO2"
    Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
    
<b>Example 3:</b>

    Input: formula = "K4(ON(SO3)2)2"
    Output: "K4N2O14S4"
    Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.

<b>Constraints:</b>

- 1 <= formula.length <= 1000
- formula consists of English letters, digits, '(', and ')'.
- formula is always valid.

<h2>Solution</h2>

```python
class Solution(object):
    def countOfAtoms(self, formula):
        N = len(formula)
        stack = [collections.Counter()]
        i = 0
        while i < N:
            if formula[i] == '(':
                stack.append(collections.Counter())
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < N and formula[i].isdigit(): i += 1
                multiplicity = int(formula[i_start: i] or 1)
                for name, v in top.items():
                    stack[-1][name] += v * multiplicity
            else:
                i_start = i
                i += 1
                while i < N and formula[i].islower(): i += 1
                name = formula[i_start: i]
                i_start = i
                while i < N and formula[i].isdigit(): i += 1
                multiplicity = int(formula[i_start: i] or 1)
                stack[-1][name] += multiplicity

        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                       for name in sorted(stack[-1]))
```
