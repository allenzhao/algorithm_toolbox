# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    if to < 2:
        return to
    if from_ == 0:
        return fibonacci_sum_naive(to)
    res = fibonacci_sum_naive(to) - fibonacci_sum_naive(from_-1)
    if res < 0:
        res += 10
    return res

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
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))