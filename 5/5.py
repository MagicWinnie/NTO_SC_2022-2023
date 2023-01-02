n, t = map(int, input().split())
working_times = []
for i in range(n):
    a, b = map(int, input().split())
    working_times.append((a, b))
approved = []
working_times.sort(key=lambda p: p[0])
approved.append(working_times.pop(0))
for working in working_times:
    if working[0] >= approved[-1][1]:
        approved.append(working)
time = 0
for i in range(1, len(approved)):
    time += approved[i][0] - approved[i - 1][1]
print(time)
