from typing import Dict, List, Tuple


class Board:
    def __init__(self, base: int, fence: int, trap: int, cannon: int, tower: int):
        self.available: Dict[str, int] = {
            'B': base,
            'F': fence,
            'R': trap,
            'C': cannon,
            'T': tower
        }
        self._keys_sorted = 'TCRF'
        self.board: List[str] = ['=' for _ in range(20)]
        self.put_bases()

    def put_bases(self):
        if self.available['B'] == 1:
            self.board[9] = 'B'
        elif self.available['B'] == 2:
            self.board[9] = 'B'
            self.board[10] = 'B'
        elif self.available['B'] == 3:
            self.board[8] = 'B'
            self.board[9] = 'B'
            self.board[10] = 'B'
        self.available['B'] = 0

    def put_symmetry(self, structure: str, position: int) -> bool:
        if self.board[position] == 'B' or self.board[20 - position - 1] == 'B' or self.available[structure] < 2:
            return False
        self.board[position] = structure
        self.board[20 - position - 1] = structure
        self.available[structure] -= 2
        return True
    
    def put(self, structure: str, position: int) -> bool:
        if self.board[position] == 'B' or self.available[structure] < 1:
            return False
        self.board[position] = structure
        self.available[structure] -= 1
        return True

    def put_structures_heading_right(self, structures: str, position: int) -> bool:
        for i in range(len(structures)):
            if position + i >= 20 or self.board[position + i] != '=':
                return False
        for structure in self.available:
            if structures.count(structure) > self.available[structure]:
                return False
        for i in range(len(structures)):
            self.board[position + i] = structures[i]
            self.available[structures[i]] -= 1
        return True

    def put_structures_heading_left(self, structures: str, position: int) -> bool:
        for i in range(len(structures)):
            if position - i < 0 or self.board[position - i] != '=':
                return False
        for structure in self.available:
            if structures.count(structure) > self.available[structure]:
                return False
        for i in range(len(structures)):
            self.board[position - i] = structures[i]
            self.available[structures[i]] -= 1
        return True

    def put_structures_symmetry(self, structures: str, position: int) -> Tuple[bool, bool]:
        if self.get_empty_left() >= self.get_empty_right() - 2:
            res1 = self.put_structures_heading_right(structures, position)
            res2 = self.put_structures_heading_left(structures, 20 - position - 1)
        else:
            res2 = self.put_structures_heading_left(structures, 20 - position - 1)
            res1 = self.put_structures_heading_right(structures, position)
        return (res1, res2)

    def put_remaining(self):
        i = 9
        while i != 1:
            if self.get_empty_left() >= self.get_empty_right() - 2 and self.board[i] == '=':
                for structure in self._keys_sorted:
                    if self.available[structure] > 0:
                        self.board[i] = structure
                        self.available[structure] -= 1
                        break
                else:
                    break
            if self.get_empty_left() <= self.get_empty_right() - 2 and self.board[20 - i - 1] == '=':
                for structure in self._keys_sorted:
                    if self.available[structure] > 0:
                        self.board[20 - i - 1] = structure
                        self.available[structure] -= 1
                        break
                else:
                    break
            i -= 1

    def get_empty_left(self) -> int:
        return self.board[0:10].count('=')

    def get_empty_right(self) -> int:
        return self.board[10:20].count('=')

    def __str__(self) -> str:
        return ''.join(self.board)
        


def solution(hp: int, dmg: int, base: int, fence: int, trap: int, cannon: int, tower: int) -> str:
    board = Board(base, fence, trap, cannon, tower)

    i = 1
    while True:
        if board.put_structures_symmetry('FC', i) == (False, False):
            break
        i += 2
    while True:
        if board.put_structures_symmetry('FT', i) == (False, False):
            break
        i += 2
    while True:
        if board.put_structures_symmetry('CC', i) == (False, False):
            break
        i += 2
    while True:
        if board.put_structures_symmetry('RF', i) == (False, False):
            break
        i += 2
    while True:
        if board.put_structures_symmetry('RFC', i) == (False, False):
            break
        i += 3
    while True:
        if board.put_structures_symmetry('RFT', i) == (False, False):
            break
        i += 3
    while True:
        if board.put_structures_symmetry('RFFFT', i) == (False, False):
            break
        i += 5
    while True:
        if board.put_structures_symmetry('RFFFC', i) == (False, False):
            break
        i += 5
    
    board.put_remaining()

    return str(board)


if __name__ == "__main__":
    hp, dmg = map(int, input().split())
    base, fence, trap, cannon, tower = map(int, input().split())
    print(solution(hp, dmg, base, fence, trap, cannon, tower))
