from solution import solution
from simulation import simulation

hp, dmg = map(int, input().split())
base, fence, trap, cannon, tower = map(int, input().split())

answer = solution(hp, dmg, base, fence, trap, cannon, tower)
print(simulation(hp, dmg, base, fence, trap, cannon, tower, answer))
print(answer)
