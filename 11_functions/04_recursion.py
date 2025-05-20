
# The Fibonacci series is the sequence where each number is the sum of the previous two numbers of the sequence. The first two numbers are 0 and 1 .

# The sequence appears as follows: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.

def fib(n):
    if(n==0 or n==1):
        return n
    
    return (fib(n-2)+fib(n-1))

print(fib(3))