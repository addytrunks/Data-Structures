# Iterative
def fibonacciIterative(n):
    arr = [0,1]
    for i in range(n-1):
        c = arr[i] + arr[i+1]
        arr.append(c)
    return arr

# Recursive O(2^N)
def fibonacciRecursive(n):
    if n < 2:
        return n
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)
