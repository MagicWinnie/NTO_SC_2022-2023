from itertools import combinations


n = int(input())
receivers_no = list(map(int, input().split()))
generators_no = list(range(1, n + 1))
generators_power = list(map(int, input().split()))

# set of all generators that are unusable
unusable_str = set()
for i in range(n):
    # i -- index of receiver_no
    for j in range(n):
        # j -- index of receiver_no
        if i == j:
            continue
        if (j < i and receivers_no[j] < receivers_no[i]) or (j > i and receivers_no[j] > receivers_no[i]):
            continue
        else:
            unusable_str.add(f'{receivers_no[i]}{receivers_no[j]}')

s = 0
c = 0
for r in range(1, n + 1):
    for comb in combinations(generators_no, r):
        comb_str = ''.join(map(str, comb))
        for elem in unusable_str:
            if elem in comb_str:
                break
        else:
            curr_s = 0
            curr_c = 0
            for el in comb:
                curr_s += generators_power[el - 1]
                curr_c += 1
            if curr_s > s:
                s = curr_s
                c = curr_c

print(s, c)
