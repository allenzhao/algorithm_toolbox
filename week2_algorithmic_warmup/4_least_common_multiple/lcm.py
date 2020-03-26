# Uses python3
import sys

def lcm_naive(a, b):
    return (a * b) // gcd_naive(a,b)

def gcd_naive(a, b):
    if (b == 0):
        return a
    aprime = a % b
    return gcd_naive(b, aprime)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

