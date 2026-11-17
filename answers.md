
# CMPS 2200 Recitation 07
## Answers

**Name:** Shiqian Zhang

### 2) Work of Recursive Fibonacci

The recurrence for the work of the recursive Fibonacci algorithm is:

W(n) = W(n-1) + W(n-2) + O(1)

with W(0) = W(1) = O(1).

The algorithm recursively computes both F(n-1) and F(n-2), which leads to repeated calculations.

This recurrence grows exponentially, and its solution is:

W(n) = Theta(phi^n)

where phi = (1 + sqrt(5)) / 2.

Therefore, the recursive algorithm has exponential work.

### 3) Span of Recursive Fibonacci

Assuming the two recursive calls can run in parallel, the span recurrence is:

S(n) = max(S(n-1), S(n-2)) + O(1)

Since S(n-1) >= S(n-2), we have:

S(n) = S(n-1) + O(1)

Therefore:

S(n) = Theta(n)

The span is linear because the longest chain of dependent recursive calls has length proportional to n.

### 4) Pattern in the Counts List

When n = 10, the counts list is:

[34, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1]

An interesting pattern is that the counts follow Fibonacci numbers in reverse order, with the first element being an exception.

For example, F(1) is computed 55 times, F(2) is computed 34 times, and F(3) is computed 21 times.

This pattern shows that smaller Fibonacci numbers are computed repeatedly, resulting in a large amount of duplicate work.

### 6) Work and Span of Top-Down Fibonacci

In the top-down implementation, each Fibonacci value is computed only once and stored in the fibs list.

For any i, fib_top_down(i) is called at most twice when computing F(n), because subsequent calls can use the cached result.

Each Fibonacci value requires only constant work after its smaller values have been computed.

Therefore, the total work is:

W(n) = Theta(n)

The computation still has a chain of dependencies from smaller Fibonacci numbers to larger ones, so the span is:

S(n) = Theta(n)

Memoization reduces the work from exponential to linear by avoiding repeated calculations.

### 8) Work and Span of Bottom-Up Fibonacci

In the bottom-up implementation, the Fibonacci numbers are computed iteratively and stored in a list.

Each F(i) is read from the list at most twice when computing later Fibonacci numbers.

Each iteration performs constant work, and there are O(n) iterations.

Therefore:

W(n) = Theta(n)

Since each iteration depends on values computed in previous iterations, the span is also:

S(n) = Theta(n)

The bottom-up algorithm avoids recursion and computes each Fibonacci number only once.

Both dynamic programming approaches achieve linear work and linear span, which is a significant improvement over the exponential work of the original recursive algorithm.
