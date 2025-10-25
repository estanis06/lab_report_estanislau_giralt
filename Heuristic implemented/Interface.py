import tkinter as tk
from Node import Node, Board

moves = [
    [[1, 3], [0, 2, 4], [1, 5]],
    [[0, 4, 6], [1, 3, 5, 7], [2, 4, 8]],
    [[3, 7], [4, 6, 8], [5, 7]]
]

class App(tk.Tk):
    def __init__(self, *args, **kargs):
        tk.Tk.__init__(self, *args, **kargs)
        self.geometry('650x800')
        self.container = tk.Frame(self, bg='red')
        self.container.place(relx=0, rely=0, relheight=1, relwidth=1)
        fTab = Frame_Board(self.container, self)
        fTab.tkraise()

class Ficha:
    contador = 0

    def __init__(self, r, c, n, frame):
        self.frame = frame
        self.r = r 
        self.c = c
        self.n = n 
        self.contador = Ficha.contador  
        Ficha.contador += 1

        if n != 0:
            self.button = tk.Button(
                self.frame,
                text=str(self.n),
                font=("Impact", 100),
                command=lambda: frame.move(self.contador,self.r,self.c)
            )
        else:
            self.button = tk.Button(
                self.frame,
                text='',
                font=("Impact", 100),
                command=lambda: frame.move(self.contador,self.r,self.c)
            )

        self.button.place(
            relx=1/26 + self.c * (4/13),
            rely=0.05 + self.r * (1/4),
            relheight=1/4,
            relwidth=4/13
        )

class Frame_Board(tk.Frame):
    def __init__(self, parent, root):
        self.root = root
        tk.Frame.__init__(self, parent, bg='black') 
        self.place(relx=0, rely=0, relheight=1, relwidth=1)

        b_solve = tk.Button(
            self,
            text="Solve",
            command=self.solve_click,
            background='black',
            fg='white',
            padx=10,
            pady=10
        )
        b_solve.place(relx=0.3, rely=0.85, relheight=0.1, relwidth=0.4)

        self.nums = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.aux_Board = Board(self.nums) 

        self.fichas = []
        for ir, r in enumerate(self.nums):
            for ic, c in enumerate(r):
                aux = Ficha(ir, ic, c, self)
                self.fichas.append(aux)

    def solve_click(self):
        from Node import Node 

        root = Node(nums=self.aux_Board.nums)

        steps = Node.solve(root)

        print(f"Solution found in {len(steps) - 1} movements")

        for step in steps:
            self.actualizar(step.Board.nums)
            self.update()         
            self.after(300)    


    def move(self, icontador, fr, fc):
        er, ec = self.aux_Board.empty()

        if icontador in moves[er][ec]:
            if er == fr:
                if fc < ec:
                    auxm = 'l'
                else:
                    auxm = 'r'
            else:
                if fr < er:
                    auxm = 'u'
                else:
                    auxm = 'd'

            self.aux_Board.make_move(auxm)
            self.actualizar(self.aux_Board.nums)
    def actualizar(self, nums):
        aux = 0
        for ir, r in enumerate(nums):
            for ic, c in enumerate(r):
                if c != 0:
                    self.fichas[aux].button.config(
                        text=str(c),
                        background='black',
                        fg='white',
                        borderwidth=10,
                        relief='raised'
                    )
                else:
                    self.fichas[aux].button.config(
                        text='',
                        background='white',
                        bd=5,
                        highlightcolor='white',
                        borderwidth=5
                    )
                aux += 1


if __name__ == "__main__":
    APP = App()
    APP.mainloop()
