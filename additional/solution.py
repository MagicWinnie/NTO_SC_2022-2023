from typing import List


def solution(hp: int, dmg: int, base: int, fence: int, trap: int, cannon: int, tower: int) -> str:
    answer: List[str] = ['=' for _ in range(20)]

    # bases
    if base == 2:
        answer[9] = 'B'
        answer[10] = 'B'
    elif base == 1:
        answer[9] = 'B'
    elif base == 3:
        answer[8] = 'B'
        answer[9] = 'B'
        answer[10] = 'B'
    base = 0

    # trap + fence + fence + fence + tower
    i = 1
    while trap >= 2 and fence >= 6 and tower >= 2:
        answer[i] = 'R'
        trap -= 1
        answer[20 - i - 1] = 'R'
        trap -= 1
        i += 1
        for _ in range(3):
            answer[i] = 'F'
            fence -= 1
            answer[20 - i - 1] = 'F'
            fence -= 1
            i += 1
        answer[i] = 'T'
        tower -= 1
        answer[20 - i - 1] = 'T'
        tower -= 1
        i += 1
    # trap + fence + fence + fence + cannon
    while trap >= 2 and fence >= 6 and cannon >= 2:
        answer[i] = 'R'
        trap -= 1
        answer[20 - i - 1] = 'R'
        trap -= 1
        i += 1
        for _ in range(3):
            answer[i] = 'F'
            fence -= 1
            answer[20 - i - 1] = 'F'
            fence -= 1
            i += 1
        answer[i] = 'C'
        cannon -= 1
        answer[20 - i - 1] = 'C'
        cannon -= 1
        i += 1
    # trap + fence + cannon
    while trap >= 2 and fence >= 2 and cannon >= 2:
        answer[i] = 'R'
        trap -= 1
        answer[20 - i - 1] = 'R'
        trap -= 1
        i += 1
        answer[i] = 'F'
        fence -= 1
        answer[20 - i - 1] = 'F'
        fence -= 1
        i += 1
        answer[i] = 'C'
        cannon -= 1
        answer[20 - i - 1] = 'C'
        cannon -= 1
        i += 1
    # trap + fence + tower
    while trap >= 2 and fence >= 2 and tower >= 2:
        answer[i] = 'R'
        trap -= 1
        answer[20 - i - 1] = 'R'
        trap -= 1
        i += 1
        answer[i] = 'F'
        fence -= 1
        answer[20 - i - 1] = 'F'
        fence -= 1
        i += 1
        answer[i] = 'T'
        tower -= 1
        answer[20 - i - 1] = 'T'
        tower -= 1
        i += 1
    # fence + tower
    while trap >= 2 and fence >= 2 and tower >= 2:
        answer[i] = 'R'
        trap -= 1
        answer[20 - i - 1] = 'R'
        trap -= 1
        i += 1
        answer[i] = 'F'
        fence -= 1
        answer[20 - i - 1] = 'F'
        fence -= 1
        i += 1
        answer[i] = 'T'
        tower -= 1
        answer[20 - i - 1] = 'T'
        tower -= 1
        i += 1

    print(base, fence, trap, cannon, tower)
    return ''.join(answer)


if __name__ == "__main__":
    hp, dmg = map(int, input().split())
    base, fence, trap, cannon, tower = map(int, input().split())
    print(solution(hp, dmg, base, fence, trap, cannon, tower))
