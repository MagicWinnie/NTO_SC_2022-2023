from solution import solution
from simulation import simulation

f = open('tests.txt', 'r')

amount = 0
N = int(f.readline().strip())
for i, line in enumerate(f):
    hp, dmg, base, fence, trap, cannon, tower = map(int, line.strip().split())
    answer = solution(hp, dmg, base, fence, trap, cannon, tower)
    flag, points = simulation(hp, dmg, base, fence, trap, cannon, tower, answer)
    if flag:
        # print(f"Test #{i + 1}/{N} passed.")
        amount += 1
    else:
        # print(f"Test #{i + 1}/{N} not passed.")
        pass
print(f"{amount}/{N} of tests have pased.")
f.close()
