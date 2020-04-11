# Complexity Analysis

Complexity Analysis of an algorithm is concerned about how fast or slow a particular algorithm can perform. It can be defined as a numerical function T(n) - time vs. the input size n

## Asymptotic Notations

### 1. Big Oh Notation

For any **monotonic** functions f(n) and g(n) from the positive integers to the positive integers, we say that f(n) = O(g(n)) when there exists constants c > 0 and n0 > 0 such that

> f(n) <= c \* g(n), for all n >= n0

This implies that the function f(n) does not grow faster than g(n), or that function g(n) is **upper bound** for f(n), for all sufficiently n --> infinity

<div style="text-align: center";>
<img src="bigO.bmp" width="80%">
<p>Source: cs.cmu.edu</p>
</div>

> Note: Big Oh notation is not symmetric: n = O(n^2) but n^2 != O(n)
