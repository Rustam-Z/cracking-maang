# Backtracking = Brute Force Approach

## Brute Force Approach
Brute-force search (BFS) is a type of algorithm which computes every possible solution to a problem and then selects one that fulfills the requirements.

## Backtracking
- The backtracking algorithm is a systematic way to explore all possible solutions to a problem through a recursive trial-and-error approach. It is often used to solve problems where there are multiple possible solutions, and the goal is to find one or more valid solutions.
- The general idea behind the backtracking algorithm is to build a solution incrementally, one step at a time, by making choices at each step and checking if the current choice leads to a valid solution. If the choice does not lead to a valid solution, the algorithm backtracks (i.e., undoes the last choice) and explores other possibilities.
- Backtracking can be defined as a general algorithmic technique that considers searching every possible combination in order to solve a computational problem. Looks like Brute Force Approach? So, what is the difference?
- Backtracking vs brute force:
  - The difference is that backtracking is an optimization over the brute force approach, which looks for a solution by trying all possible paths and then selecting the best one. On the other hand, backtracking looks for a solution by trying all possible paths, and as soon as it finds one, it stops searching.
  - Backtracking is an extension to BFS in which the implicit constraints are evaluated after every choice (as opposed to after all solutions have been generated), which means that potential solutions can be discarded before they have been 'finished'.
- Dynamic programming = solving sub-problems to solve the main problem, remembering the real solutions. 
  But backtracking is not dynamic programming, we try all possible solutions, and if it does not work, we backtrack and try another solution.
  But both of them are solved recursively.

## Backtracking Template
```python
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
```
- Always recursion
- Choice + constraints

The backtracking algorithm typically follows these steps:
- Choose: Make a choice at the current step, usually by selecting an option from a list of possibilities. 
- Check: Verify if the current choice is valid and does not violate any constraints or conditions. 
- Explore: If the choice is valid, proceed to the next step and repeat the process recursively for the remaining subproblems. 
- Backtrack: If the choice is not valid or cannot lead to a valid solution, undo the choice (backtrack) and try other options. 
- Repeat: Continue the process of choosing, checking, exploring, and backtracking until a valid solution is found or all possibilities have been explored. 
- Backtracking is widely used in various problem-solving scenarios, such as finding a path in a maze, solving puzzles like Sudoku or N-Queens, generating all possible combinations, permutations, or subsets of a set, and many other optimization and decision problems.
