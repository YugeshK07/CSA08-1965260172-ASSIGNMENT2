# Q7 - Redesign Q6 using iteration and O(1) auxiliary space
# Original limitation: naive recursion repeats subproblems exponentially.
# Memoisation removes repeated work but recursion depth still grows with n.

def ways_memo(n, cache=None):
    if cache is None:
        cache = {0: 1, 1: 1}
    if n in cache:
        return cache[n]
    cache[n] = ways_memo(n - 1, cache) + ways_memo(n - 2, cache)
    return cache[n]

def ways_iterative(n):
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

for n in (10, 20, 25, 30, 1000):
    print(n, ways_iterative(n))
