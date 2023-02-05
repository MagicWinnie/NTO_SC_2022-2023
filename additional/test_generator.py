from random import randint


N = 1000
f = open('tests.txt', 'w')
f.write(str(N) + '\n')
for _ in range(N):
    hp = randint(1, 25)
    dmg = randint(1, 3)
    base = randint(1, 3)
    fence = randint(1, 6)
    trap = randint(1, 6)
    cannon = randint(1, 6)
    tower = randint(1, 6)
    f.write(f"{hp} {dmg} {base} {fence} {trap} {cannon} {tower}\n")
f.close()
