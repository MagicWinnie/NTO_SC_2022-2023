from itertools import permutations


def runner(k0: int, k1: int):
    a = [0 for _ in range(k0)] + [1 for _ in range(k1)]
    perms = permutations(a, r=k0+k1)
    result = set()
    max_cnt = -1
    max_eq = -1
    for el in perms:
        cnt_neq = 0
        cnt_eq = 0
        for i in range(1, len(el)):
            if el[i - 1] != el[i]:
                cnt_neq += 1
            else:
                cnt_eq += 1
        if cnt_neq > max_cnt:
            max_cnt = cnt_neq
            result = set()
            max_eq = -1
        elif cnt_neq == max_cnt:
            result.add(el)
            if cnt_eq > max_eq:
                max_eq = cnt_eq
    return max_eq, len(result)


if __name__ == "__main__":
    k0, k1 = map(int, input().split())
    print("ANSWER:", *runner(k0, k1))
