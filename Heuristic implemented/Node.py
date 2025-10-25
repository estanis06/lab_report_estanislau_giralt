from Board import Board
from copy import deepcopy

def is_in(historial, nums):
        for state in historial:
            if state == nums:
                return True
        return False

class Node:
    def __init__(self, father=None, nums=[], dir='l', heuristic='h1'): #here you can select the heuristic you want
        self.heu = heuristic
        self.father = father
        if father == None: 
            self.Board = Board(nums=nums)
        else:
            self.Board = deepcopy(father.Board) 
            self.Board.make_move(dir)

        self.h = self.Board.cost(heuristic)


    def set_childs(self):
        self.childs = []
        for _dir in self.Board.moves():
            auxN = Node(father=self, dir=_dir)
            self.childs.append(auxN)

    @staticmethod
    def freeze(board):
        """Converteix [[...],[...],[...]] -> ((...),(...),(...)) per poder fer hash"""
        return tuple(tuple(row) for row in board)



    def best_first(root):
        agenda = [root] 
        historial = [] 

        it = 0
        while True:
            it += 1

            if agenda[0].Board.isSolution():  
                break
            else:
                agenda[0].set_childs()
                aux_childs = agenda[0].childs
                historial.append(agenda[0].Board.nums) 
                agenda.pop(0)

                for ci in aux_childs:
                    if not is_in(historial, ci.Board.nums):
                        agenda.append(ci)  

                auxc = [i.h for i in agenda]
                for i in range(len(agenda)):
                    for j in range(len(agenda) - i - 1):
                        if auxc[j] > auxc[j + 1]:
                            temp = auxc[j]
                            auxc[j] = auxc[j + 1]
                            auxc[j + 1] = temp

                            temp = agenda[j]
                            agenda[j] = agenda[j + 1]
                            agenda[j + 1] = temp

        print('----- SOLUTION FOUND -----')
        print('Iterations:', it)

        return agenda[0] 

    

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

            print('Iterations:', it, '| len agenda:', len(agenda), '| visited:', len(visited))

        print('----- SOLUTION FOUND -----')
        print('Iterations:', it)
        return agenda[0]

    @staticmethod
    def solve(root):
        sol = Node.best_first(root)

        steps = []
        aux = sol
        while True:
            steps.insert(0, aux)
            aux = aux.father
            if aux is None:
                break

        return steps

    
