PROMPT = {
    'code_baseline': "Solve the following problem with python and test it against the example cases only.\n\n{x}",
    'code_brute_force': "Please solve this problem with a brute-force algorithm.\nAfter generating the code, please test it against the example cases given in the definition. Only use the example cases, don't use your own test cases.\n\n{x}\n\nInstead of defining your function in the `Solution` class, change your classname to `BruteforceSolution`. As I said before, please make sure you use the most straightforward and brute-force algorithm to solve the algorithm. Do not consider any efficiency issue, make the solution as brute-force as possible. It's okay for you to enumerate over a very large search space as long as the solution is correct. What do you think are some variables that may affect the answer and how do you think they can be enumerated?",
    'code_tag_generation': "Please solve this problem with the {tag} method.\nAfter generating the code, please test it against the example cases given in the definition. Only use the example cases, don't use your own test cases.\n\n{x}\n\nAs I said before, please make sure you use the {tag} method.",
    'data_validator': "You are given this leetcode problem. Please help me by generating a validator function `is_valid_input` that takes exactly the same inputs as the solution function and returns a boolean value indicating whether the input is valid and follows the constraints defined in the problem description. Please test your data validator by checking the validity of the example cases given in the problem description.",
    'data_generator': "You are given this leetcode problem and its test input validator `is_valid_input`. Please help me by generating an input generator function `gen_input` that randomly generates test inputs which follow the constraints defined. Your `gen_input` function should make use of `is_valid_input` by validating the generated input with it. Your function should only generate test inputs and not test outputs.",
    'data_random_generator': "You are given this leetcode problem, its random input generator `gen_input`, and its brute-force solution `BruteforceSolution`. Please help me by generating 5 random inputs with the random input generator `gen_input`. You should return a function named `random_test()` that takes several arguments to control the upper limit of the input and returns a list of 5 tuples. You do not need to generate test outputs, only generate inputs.",
    'data_tricky_generator': "You are given this leetcode problem. Please help me by generating some special and tricky test inputs by the function `special_tricky_test_inputs()` that may break the user's program. Make sure that your test inputs follow the constraints defined in the problem. Do not generate test outputs, only generate inputs.",
}

CF_PROMPT = {
    "oracle_generator":
"""
Please solve this problem with a brute-force algorithm.
After generating the code, please test it against the example cases given only, do not generate your own test cases.
When comparing outputs, please do not consider the line breaks and spaces.
If it passes the cases, please tell me, in natural language "YES" at the end of your response. Otherwise, please tell me "NO".
The last word of your output should only be "YES" or "NO", nothing else.

{problem}

### Examples

{examples}

Please feed the example inputs to the function solution as an entire string.
As I said before, please make sure you use the most straightforward and brute-force algorithm to solve the algorithm.
Do not consider any efficiency issue, make the solution as brute-force as possible.
It's okay for you to enumerate over a very large search space as long as the solution is correct.
What do you think are some variables that may affect the answer and how do you think they can be enumerated?

""",
    "data_generator": """
{problem}
You are given this problem.
You should first create an input generator function `gen_input`.
`gen_input` should take a list of arguments to control the upper limit of the input and return a single string that represents the input.
`gen_input` should only generate test inputs that follow the problem constraints.
`gen_input` should only generate test inputs and not test outputs.

You should then create an extra function `batch_gen_inputs` that takes one argument - `batch_size`.
`batch_gen_inputs` should run `gen_input` for `batch_size` times with a small upper limit to make sure that it works.
`batch_gen_inputs` should return a list of strings that represent the inputs.
```
""",

}

TAG = [
        "Array",
        "String",
        "Hash Table",
        "Math",
        "Dynamic Programming",
        "Sorting",
        "Greedy",
        "Depth-First Search",
        "Binary Search",
        "Database",
        "Breadth-First Search",
        "Tree",
        "Matrix",
        "Two Pointers",
        "Binary Tree",
        "Bit Manipulation",
        "Heap (Priority Queue)",
        "Stack",
        "Graph",
        "Prefix Sum",
        "Design",
        "Simulation",
        "Counting",
        "Backtracking",
        "Sliding Window",
        "Union Find",
        "Linked List",
        "Ordered Set",
        "Monotonic Stack",
        "Enumeration",
        "Recursion",
        "Trie",
        "Divide and Conquer",
        "Binary Search Tree",
        "Bitmask",
        "Queue",
        "Number Theory",
        "Memoization",
        "Segment Tree",
        "Geometry",
        "Topological Sort",
        "Binary Indexed Tree",
        "Hash Function",
        "Game Theory",
        "Combinatorics",
        "Shortest Path",
        "Data Stream",
        "Interactive",
        "String Matching",
        "Rolling Hash",
        "Brainteaser",
        "Randomized",
        "Monotonic Queue",
        "Merge Sort",
        "Iterator",
        "Concurrency",
        "Doubly-Linked List",
        "Probability and Statistics",
        "Quickselect",
        "Bucket Sort",
        "Suffix Array",
        "Minimum Spanning Tree",
        "Counting Sort",
        "Shell",
        "Line Sweep",
        "Reservoir Sampling",
        "Eulerian Circuit",
        "Radix Sort",
        "Strongly Connected Component",
        "Rejection Sampling",
        "Biconnected Component"
    ]