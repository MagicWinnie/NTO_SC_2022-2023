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

    patterns = {
        "FCFTT": 351,
        "FFTTT": 345,
        "FCFCT": 336,
        "RFCTT": 331,
        "FCTTT": 330,
        "CFCTT": 326,
        "FFFTT": 321,
        "RFCCT": 301,
        "RFCFT": 301,
        "RFFTT": 301,
        "FCTT": 291,
        "CCFCT": 281,
        "RFTTT": 265,
        "FCCT": 261,
        "FCFT": 261,
        "FFTT": 261,
        "FCFFT": 261,
        "FTTTT": 258,
        "RFCRT": 250,
        "RFCT": 241,
        "RFFFT": 226,
        "FTTT": 225,
        "RFRFT": 209,
        "CCCCT": 206,
        "CCCTT": 206,
        "FCT": 201,
        "RFRTT": 193,
        "FFFT": 186,
        "FFFFT": 186,
        "CCTTT": 185,
        "RFTT": 181,
        "RCCCT": 171,
        "FRFT": 169,
        "FCC": 165,
        "CCCT": 161,
        "RFC": 160,
        "RCCTT": 156,
        "TCTTT": 149,
        "CCTT": 146,
        "FTT": 141,
        "FFT": 126,
        "RRCCT": 121,
        "FC": 120,
        "FCF": 120,
        "RCTTT": 120,
        "RFRRT": 120,
        "RFRT": 115,
        "RCCT": 111,
        "TTTTT": 111,
        "CCC": 110,
        "CTTT": 110,
        "RFT": 106,
        "CCT": 101,
        "RRCTT": 94,
        "RTTTT": 84,
        "CRTT": 83,
        "TTTT": 78,
        "RCC": 75,
        "CTT": 71,
        "RRCRT": 70,
        "FT": 66,
        "CC": 65,
        "RTRTT": 63,
        "RRCT": 61,
        "TRTT": 57,
        "RCT": 51,
        "TTT": 45,
        "RRTRT": 44,
        "RFR": 42,
        "CT": 41,
        "RF": 40,
        "FRF": 40,
        "RRC": 37,
        "RTRT": 36,
        "RC": 30,
        "TRT": 30,
        "RRRRT": 27,
        "RRRT": 22,
        "TT": 21,
        "RRT": 17,
        "RT": 12,
        "RRR": 6,
        "RR": 4,
        "FF": 0,
        "FFF": 0
    }
    i = 1
    for pattern in patterns:
        while True:
            if board.put_structures_symmetry(pattern, i) == (False, False):
                break
            i += len(pattern)
    
    board.put_remaining()

    return str(board)


if __name__ == "__main__":
    hp, dmg = map(int, input().split())
    base, fence, trap, cannon, tower = map(int, input().split())
    print(solution(hp, dmg, base, fence, trap, cannon, tower))
