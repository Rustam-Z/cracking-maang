# Cracking the Coding Interview 

Rustam-Z 🚀 • 8 June 2021

Overall, it took me 1.5 years to crack the MAANG interview, including learning algorithms and data structures, practicing coding & problem-solving, and applying and passing all interviews. During this period I had interviews at Meta, and a successful interview at Bloomberg. 

> Join my Telegram channel: [@cracking_maang](https://t.me/cracking_maang), where I share MAANG interview preparation resources.

<img src="_resources/ctci.jpg">

# My Interview Preparation Roadmap 
1. Learning algorithms and data structures.
2. Solving algorithms, and learning patterns and concepts.
3. Practicing coding & problem-solving questions together with friends on the whiteboard.
4. Learning System Design (*I will write a separate article about System Design*).
5. Writing a resume. 
6. Applying to jobs.
7. Preparing for a behavioral interview.
8. Getting an interview invitation, passing all interviews, and getting an offer! 🍾

# Learning Algorithms and Data Structures  
1. I had a Data Structures class at university. [Here are the notes from the class.](https://github.com/Rustam-Z/data-structures-and-algorithms)
2. [Naso Academy DS playlist](https://www.youtube.com/playlist?list=PLBlnK6fEyqRj9lld8sWIUNwlKfdUoPd1Y)
3. [Jenny's DSA playlist](https://www.youtube.com/playlist?list=PLdo5W4Nhv31bbKJzrsKfMpo_grxuLl8LU)
4. [Programiz.com/dsa](https://www.programiz.com/dsa)
5. [Data Structures by a Google Software Engineer](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu)
6. NeetCode videos: [here’s one of them](https://youtu.be/uhYq27iSk9s?feature=shared)
7. AlgoExpert Data Structures course
8. Extra:
    - [The Last Algorithms Course You'll Need](https://frontendmasters.com/courses/algorithms/introduction/)
    - [Tech Interview Handbook Algorithms Cheat Sheet](https://www.techinterviewhandbook.org/algorithms/study-cheatsheet/)


# System Design Learning Plan
1. "Systems Expert" from AlgoExpert
2. "System Design Interview" book - 1<sup>st</sup> and 2<sup>nd</sup> editions
3. "Grokking the System Design Interview" (educative.io)
4. "Designing Data-Intensive Applications" book
5. [Tushar](https://www.youtube.com/user/tusharroy2525/playlists)


# Data Structure Topics to Learn 
- Big-O = **how quickly the runtime grows relative to the input as the input gets arbitrarily large.**
- Strings
    - ASCII, Unicode
    - How are strings implemented in your programming language (for example, is there a maximum length)?
    - Search for substrings (for example, the Rabin-Karp algorithm).
    - RegEx
- Arrays. Details of implementation in your programming language. For example, for C++ you need to know the implementation using pointers, and vectors. For vectors, you also need to know, for example, that it periodically does resize, and other similar details.
- Sorting algorithms. Especially make sure you know heap sort, merge sort and quick sort.
- Searching algorithms. Binary search.
- Linked lists
    - Singly linked list
    - Doubly linked list
    - Algorithm: Fast and slow pointer
    - Algorithm: Pointers with next
    - Algorithm: Searching in linked lists
- Stacks and Queues
- Trees
    - DFS (must learn)
    - BFS (must know)
    - Preorder (must know)
    - Postorder
    - Inorder
    - Recursive and iterative problem solving
    - Adding and removing elements
    - Less common tree types (e.g., red black trees, B-trees) - what are they, how they differ from the binary trees, basic complexities, and how they are used. No need to know all the rotations in the RB-tree, for example.
    - Tries
- Heaps
    - Heap sort
    - Using heaps for tracking top-K
    - Allocating elements on a heap vs on a stack - what does it mean?
- Graphs
    - DFS, BFS
    - Topological search
    - Shortest path
- Hash
    - Hash functions
    - Universal hash
- Algorithmic Paradigms
    - Brute Force
    - Greedy Algorithms
    - Divide and Conquer
    - Dynamic programming
- Dynamic programming = problems, which are problems where the solution is composed of solutions to the same problem with smaller inputs.
    - Recursion
    - Memoisation
    - Backtracking = Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time.
    - Button up
    - Top down
 
# Practicing Coding & Problem Solving
1. [Interviewbit.com](https://www.interviewbit.com/courses/programming/)
2. [LeetCode Explore](https://leetcode.com/explore/) (only data structures cards)
3. [LeetCode Study Plan](https://leetcode.com/study-plan/) — [Data Structure 1, Algorithm 1, Programming Skills 1](https://gist.github.com/priyavrat-misra/a776a005ee4a68edda535f4a7e1b6adb)
4. "Cracking the Coding Interview" + [CTCI problems in LeetCode](https://leetcode.com/discuss/general-discussion/1152824/cracking-the-coding-interview-6th-edition-in-leetcode)
5. [LeetCode Study Plan](https://leetcode.com/study-plan/) — [Data Structure 2, Algorithm 2, Programming Skills 2](https://gist.github.com/priyavrat-misra/a776a005ee4a68edda535f4a7e1b6adb)
6. AlgoExpert video solutions
7. [Neetcode.io](https://neetcode.io/) & [NeetCode playlist](https://www.youtube.com/c/NeetCode/playlists)
    1. Start with https://neetcode.io/practice?tab=neetcode250 250 if you have 0 knowledge in DS & A, otherwise start with TOP 150.
8. LeetCode company-tagged questions, check LeetCode discussions, check Team Blind, check Glassdoor for recently asked questions.

# Top Coding Interview Concepts

List of patterns to solve algorithms:
https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed

Top coding interview concepts:

1. Heap top=O(1), insert=O(log n), remove=O(log n), heapify=O(n)
2. Sliding window, two pointers
3. Binary search O(log n)
4. DFS & BFS
5. Recursion (trees, graphs, backtracking, DP and more)
6. HashMaps search=O(1), insert=O(1), remove=O(1)

# Problem-Solving Approach

**Constraints, Ideas, Complexities, Code, and Tests**

1. Read the problem. Don’t immediately jump into coding!
2. Understand inputs and outputs. Draw some examples on paper.
3. Clarify requirements, ask questions (I am providing the list of questions below), and find constraints (edge cases). Example questions: Is it ASCII or Unicode? What is the max value? Is there a difference between capital letters and small letters?
4. Think about the solution in your mind. Divide problems into sub-problems. Come up with different ideas (ask whys, think about trade-offs, solve simpler versions, imagine helper functions - go from high level to low level).
5. Evaluate the complexity and trade-offs.
6. Think of a better alternative solution.
7. Write code on paper.
8. Debug your code on paper and test with new corner case inputs.
9. Write code. Write clean code.
10. Write tests. Positive, negative, with edge-cases.

**More to read:**

- [HiredInTech Algorithm Design Canvas](https://www.hiredintech.com/algorithms/algorithm-design-canvas/what-is-the-canvas/)

# Questions: Corner Cases and Constraints

1. Ask about edge cases (propose edge case). Explain and clarify, DS tradeoff, time and space complexity.
2. Questions
    1. How am I receiving this data?
    2. How should I output the result?
    3. What if wrong input is provided?
        
        How long/big our input could be? 
        
        **Empty inputs, null values, 0 length, 1 element input, super long input.**
        
3. Is size, speed, using not build-in library a concern?
4. How I would be testing? Tests: Zero, one, two, two to max-1, max, max+1
5. Questions to ask
    - OOP
        - how many call will we get for each?
        - Do we need caching if similar calls or similar work needs to be done?
        - what if the data object is empty before calling the remove/pop/top methods?
    - Number (int, float)
        1. what if we have floats?
        2. zero? 
        3. Can we have negative/positive numbers? 
        4. what is the range on integer? max and min integer?
        5. dividing by zero?
        6. do we have leading 0s?
        7. Can we use bit manipulation? XOR?
    - Strings
        1. ASCII, Unicode UTF-8 (special chars)? Character encoding standards. `ProTip™, 👻, 60%, https://google.com`
        2. Only lower-case English characters, or? How to handle them?
        3. what if the string is empty, “ “, NULL, length is 1?
        4. spaces in string in the beginning or in the end?
        5. max and min length of string?
        6. sorted? can we sort it?
        7. DS: Can we use stack, queue, heap? If duplicates maybe use stack?
    - Array
        1. Mutable or immutable array?
        2. Should it be in place? Or we need to return new one?
        3. Items in array are all unique?
        4. Do we have repeated items in array? OR can I use the same element twice?
        5. Does array contain NULLs?
        6. How to handle an empty array?
        7. What would I do if the array is super large.
        8. Can we sort the array?
        9. Do we need to preserve ORDER?
    - Sorting algorithm
        1. empty input, null input
        2. 1 element, very long input
        3. duplicate elements (sort on a second condition?)
        4. odd/even length input
        5. Collection with all elements equal?
        6. Garbage inside the collection?
    - Stack/queue
        1. removing elements from empty stack/queue
    - Linked list
        1. Single linked list or doubly linked list?
        2. Is it a circular linked list?
        3. How many nodes does the linked list contain?
        4. Null values for head/root 
        5. Can it be empty?
        6. Values are sorted? Are there any duplicate numbers?
        7. Can I convert it to array?
    - Tree
        
        ```python
        1. Edge = link between any two nodes.
        2. Height of node = number of edges from the deepest leaf to node.
        3. Depth of a node = number of edges from the root to the node.
        4. Height of a tree = height of the root node.
        ```
        
        1. Is it a Binary Tree? (Each node has at most two children.)
        2. Is it a Binary Search Tree (BST)? (Left child is less than the parent, and right child is greater.)
        3. If BST do we have duplicates? And in which side?
        4. Height of the tree? (Longest path from a leaf node to root.)
        5. Depth of a specific node? (Length of the path from the root to that node.)
        6. Is it a Balanced Tree? (Height of left and right subtrees differ by at most 1. Ensuring `O(logn)` for insert and find)
        7. Is it a Complete Binary Tree? (All levels are filled, except possibly the last one, and nodes are left-justified.)
        8. Is it a Full Binary Tree? (Each node has either 0 or 2 children.)
        9. Is it a Perfect Binary Tree? (All internal nodes have two children, and all leaves are at the same level.)
        10. Is it a Binary Heap? (Specifically for Binary Trees that follow the heap property.)
        11. Is it a Symmetric Tree (or Mirror Tree)? (The left subtree of one node is a mirror image of the right subtree of the other node.)
    - Graph
        - Directed (one-way street) or undirected (two-way)?
        - Connected graph(undirected graph, there is always a path to the node) or not-connected?
        - Strongly connected graph (directed graph, when there is always a route)
        - Cyclic or Acyclic? (Does the graph contain any cycles, or is it a directed acyclic graph (DAG)?)
        - Weighted or Unweighted? (Are there numerical values assigned to the edges?)
        - Tree or Forest? (Is the graph a connected acyclic graph, or is it a collection of disconnected trees?)
        - Complete or Incomplete? (Does every pair of distinct vertices have an edge between them?) From any node (vertex) you can do to any node.
        
        ---
        
        - Should I use DFS or BFS?
        - Dijkstra?
    - Loops
        1. while loops running forever (properly incre./decre. pointers)
    - Recursion
        1. recursion 1.000 call stack size is input it too big?
6. Extra: [Taking the Edge Off of Edge Cases](https://medium.com/swlh/taking-the-edge-off-of-edge-cases-7b3008d83a57)

# **General Tips**

Interviews are not only about evaluating your technical knowledge. Explain your thought process and show how you approach problem-solving in a structured way step by step. 

Many questions asked by interviewers are open-ended, so ask good questions to clarify a full set of criteria to solve the problem and clarify requirements. 

Always, always, always ask clarifying questions before jumping to a solution. 

Try thinking of different solutions to a given problem and explain why you came up with this solution or this code. Compare your solutions, compare complexities, and think about their trade-offs. 

Overall, the interview should be like a dialogue — show how it is to work with you, how collaborative you are.

# **Must Watch and Must Read Resources**

- [Interview Cake Coding Interview Tips](https://www.interviewcake.com/coding-interview-tips)
- [Prepare for Your Google Interview: Coding](https://youtu.be/6ZZX9iIgFoo?feature=shared)
- [Interview tips from Google Software Engineers](https://youtu.be/XOtrOSatBoY?feature=shared)
- [Coding Mock Interview](https://www.youtube.com/watch?v=XKu_SEDAykw)

# **Extra resources to Watch and to Read**

- [Tech Interview Process](https://youtu.be/nemEAjYcdo0?feature=shared)
- [Preparing for a Technical Interview](https://youtu.be/OMkfujDPpwc?feature=shared)
- [Prepare for your Google Interview: General Cognitive Ability](https://youtu.be/eIMR82oO2Dc?feature=shared)
- [Prepare for your Google Interview: Leadership](https://youtu.be/2Cr3-et4xkI?feature=shared)
- ["100ta Intervyu Nima O'rgatdi?" by Azimjon](https://azimjon.com/blog/100ta-intervyu-nima-orgatdi/)
