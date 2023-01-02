from math import factorial


def C(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def runner(k0: int, k1: int):
    if k0 > k1:
        k0, k1 = k1, k0
    if k0 == k1:
        return 0, 2
    return max(0, k1 - k0 - 1), C(k1 - 1, k0)


if __name__ == "__main__":
    k0, k1 = map(int, input().split())
    print(*runner(k0, k1))

# wrong answer at 3 3