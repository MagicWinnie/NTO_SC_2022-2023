def getColumn(lists, column):
    res = []
    for l in lists:
        res.append(l[column])
    return res

n, k = map(int, input().split())
elems = []
group = []
weight = []
for i in range(n):
    # i + 1 -- amount of money
    boost = list(map(int, input().split())) # length of k
    for j in range(k):
        elems.append(boost[j])
        group.append(j)
        weight.append(i + 1)

elems, group, weight = zip(*sorted(zip(elems, group, weight), key=lambda x:x[1]))

dp = [[0 for _ in range(n + 1)] for _ in range(len(elems) + 1)] 

for w in range(n + 1):
    for i in range(len(elems) + 1):
        if i == 0 or w == 0: 
            dp[i][w] = 0
        elif weight[i - 1] <= w: 
            sub_max = 0
            prev_group = group[i - 1] - 1
            sub_dp = getColumn(dp, w - weight[i - 1])
            for j in range(len(elems) + 1):
                if group[j - 1] == prev_group and sub_dp[j] > sub_max:
                    sub_max = sub_dp[j]
            dp[i][w] = max(sub_max + elems[i - 1], dp[i - 1][w]) 
        else: 
            dp[i][w] = dp[i - 1][w]

print(dp[len(elems)][n])
