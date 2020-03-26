# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    period = get_pisano_per (n, m)
    remainder = n % period
    return fib_naive(remainder, m)

def fib_naive(n, m):
    if (n <= 1):
        return n
    F = [0] * (n+1)
    F[1] = 1
    for i in range(2,n+1):
        F[i] = (F[i-1] + F[i-2]) % m
    return F[n]

# Credit: https://www.coursera.org/learn/algorithmic-toolbox/discussions/weeks/2/threads/7eKhCEHZEeaPHQrkCWo3rw/replies/WJnGPK_5SjOZxjyv-SozCg/comments/D8n4U0HIToCJ-FNByI6A1g
def get_pisano_per(n, m):
    fib_series = [0,1]
    period = 0
    while True:
        fib_series.append((fib_series[-1] + fib_series[-2]) % m)
        if fib_series[-2:] == [0,1]:
            period = len(fib_series) - 2
            break
    return period

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
