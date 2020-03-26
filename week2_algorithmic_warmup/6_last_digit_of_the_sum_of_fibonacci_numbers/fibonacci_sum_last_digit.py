# Uses python3
import sys

#Credit: https://stackoverflow.com/a/57052717
def fibonacci_sum_naive(n):
    period = 60
    if n < 2:
        return n
    n %= period
    fib = [1, 1]
    for i in range(n):
        fib.append((fib[-1] + fib[-2]) % 10 )
    return (fib[-1] - 1) % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
