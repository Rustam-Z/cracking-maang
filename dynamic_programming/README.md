# Dynamic Programming

"Those who cannot remember the past are condemned to repeat it." - Dynamic Programming

## What is Dynamic Programming?
- Dynamic programming amounts to breaking down an **optimization problem** into simpler sub-problems, kand storing the solution to each sub-problem so that each sub-problem is only solved once.
- The goal of DP is to solve the problem by combining solutions to these sub-problems, never solving the same sub-problem twice.
- Dynamic programming is an optimization technique for recursive solutions. 

## Types of DP techniques
There are two main types of dynamic programming:
1. **Memoization** (Top-down): 
    The memoized program for a problem is similar to the recursive version with a small modification that it looks 
    into a lookup table before computing solutions. We initialize a lookup array with all initial values as NIL. 
    Whenever we need the solution to a sub-problem, we first look into the lookup table. If the precomputed value 
    is there then we return that value, otherwise, we calculate the value and put the result in the lookup table 
    so that it can be reused later.
2. **Tabulation** (Bottom-up): 
    The tabulated program for a given problem builds a table in bottom-up fashion and returns the last entry from the table. 
    For example, for the same Fibonacci number, we first calculate fib(0) then fib(1) then fib(2) then fib(3) and so on. 
    So literally, we are building the solutions of sub-problems bottom-up.
3. **Memoization vs Tabulation**: The two methods mainly differ in the approach of the subproblem solutions. In the case of memoization, the subproblem solutions are saved for the same inputs in a lookup table. However, in the case of tabulation, the sub-problem is solved and the solution is tabulated.

## How to approach a DP problem?
1. Identify the sub-problem in words.
2. Write out the sub-problem as a recurring mathematical decision. Identify the base case, and the recursive case.
3. Solve the original problem using Steps 1 and 2.
4. Apply memoization or tabulation to optimize the solution.
