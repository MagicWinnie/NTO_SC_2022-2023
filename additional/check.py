from solution import solution
from simulation import simulation

hp, dmg = map(int, input().split())
base, fence, trap, cannon, tower = map(int, input().split())

print(simulation(hp, dmg, base, fence, trap, cannon, tower, solution(hp, dmg, base, fence, trap, cannon, tower)))
