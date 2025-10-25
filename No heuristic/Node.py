from Board import Board
from copy import deepcopy

class Node:
    def __init__(self, father=None, nums=[], dir='l'):
        self.father = father
        if self.father is None:
            self.Board = Board(nums)
        else:
            self.Board = deepcopy(self.father.Board)
            self.Board.make_move(dir=dir)

    def set_childs(self):
        self.childs = []
        for _dir in self.Board.moves():
            auxN = Node(father=self, dir=_dir)
            self.childs.append(auxN)

    @staticmethod
    def freeze(board):

        return tuple(tuple(row) for row in board)

    @staticmethod
    def breadth_first(root):
        agenda = [root]
        visited = set()
        visited.add(Node.freeze(root.Board.nums))

        it = 0
        while True:
            it += 1
            node = agenda[0]

            if node.Board.isSolution():
                break

            node.set_childs()
            for child in node.childs:
                key = Node.freeze(child.Board.nums)
                if key not in visited:
                    visited.add(key)
                    agenda.append(child)

            agenda.pop(0)


        print('----- SOLUTION FOUND -----')
        print('Iterations:', it)
        return agenda[0]

    @staticmethod
    def solve(root):
        sol = Node.breadth_first(root)

        steps = []
        aux = sol
        while True:
            steps.insert(0, aux)
            aux = aux.father
            if aux is None:
                break

        return steps
