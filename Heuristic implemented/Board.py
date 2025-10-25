sol = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

moves_list = [
    [['r', 'd'], ['l', 'r', 'd'], ['l', 'd']],
    [['r', 'u', 'd'], ['l', 'r', 'u', 'd'], ['l', 'u', 'd']],
    [['r', 'u'], ['l', 'r', 'u'], ['l', 'u']]
]

class Board:
    def __init__(self, nums=[[1, 2, 3], [4, 5, 6], [7, 8, 0]]):
        self.nums = nums

    def isSolution(self):
        return self.nums == sol

    def empty(self):
        for ir, r in enumerate(self.nums):
            for ic, c in enumerate(r):
                if c == 0:
                    return ir, ic

    def moves(self):
        r, c = self.empty()
        return moves_list[r][c]

    def make_move(self, dir):
        r, c = self.empty()

        if dir == 'l':
            aux = self.nums[r][c]
            self.nums[r][c] = self.nums[r][c - 1]
            self.nums[r][c - 1] = aux

        elif dir == 'r':
            aux = self.nums[r][c]
            self.nums[r][c] = self.nums[r][c + 1]
            self.nums[r][c + 1] = aux

        elif dir == 'u':
            aux = self.nums[r][c]
            self.nums[r][c] = self.nums[r - 1][c]
            self.nums[r - 1][c] = aux

        elif dir == 'd':
            aux = self.nums[r][c]
            self.nums[r][c] = self.nums[r + 1][c]
            self.nums[r + 1][c] = aux

    def h1(self):  # number of wrong squares
        aux = 0
        for ir, r in enumerate(self.nums):
            for ic, c in enumerate(r):
                if (c != sol[ir][ic]) and c != 0:
                    aux += 1
        return aux

    def find(self, n):
        for ir, r in enumerate(sol):
            for ic, c in enumerate(r):
                if c == n:
                    return ir, ic

    def h2(self):  # manhattan distance
        aux = 0
        for ir, r in enumerate(self.nums):
            for ic, n in enumerate(r):
                if (n != sol[ir][ic]) and n != 0:
                    ir_, ic_ = self.find(n)
                    aux += abs(ir - ir_) + abs(ic - ic_)
        return aux
    
    def h3(self):  # sum of both heuristics
        return self.h1() + 0.5 * self.h2()

    def cost(self, heuristic='h1'):
        if heuristic == 'h1':
            return self.h1()
        elif heuristic == 'h2':
            return self.h2()
        elif heuristic == 'h3':
            return self.h3()
