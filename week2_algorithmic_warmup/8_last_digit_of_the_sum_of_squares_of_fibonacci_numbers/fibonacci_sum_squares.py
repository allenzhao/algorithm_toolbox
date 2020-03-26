# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n
    period = 0
    res = [0, 1]
    while True:
        res.append((res[-1] + res[-2])%10)
        if res[-2:] == [0,1]:
            period = len(res) - 2
            break
    remainder = n % period

    return (res[remainder] * res[remainder + 1]) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
