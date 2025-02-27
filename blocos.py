from bloco import Bloco
from posicao import Posicao

class BlocoL(Bloco):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [Posicao(0, 2), Posicao(1, 0), Posicao(1, 1), Posicao(1, 2)],
            1: [Posicao(0, 1), Posicao(1, 1), Posicao(2, 1), Posicao(2, 2)],
            2: [Posicao(1, 0), Posicao(1, 1), Posicao(1, 2), Posicao(2, 0)],
            3: [Posicao(0, 0), Posicao(0, 1), Posicao(1, 1), Posicao(2, 1)]
        }
        self.move(0, 3)

class BlocoJ(Bloco):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Posicao(0, 0), Posicao(1, 0), Posicao(1, 1), Posicao(1, 2)],
            1: [Posicao(0, 1), Posicao(0, 2), Posicao(1, 1), Posicao(2, 1)],
            2: [Posicao(1, 0), Posicao(1, 1), Posicao(1, 2), Posicao(2, 2)],
            3: [Posicao(0, 1), Posicao(1, 1), Posicao(2, 0), Posicao(2, 1)]
        }
        self.move(0, 3)

class BlocoI(Bloco):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Posicao(1, 0), Posicao(1, 1), Posicao(1, 2), Posicao(1, 3)],
            1: [Posicao(0, 2), Posicao(1, 2), Posicao(2, 2), Posicao(3, 2)],
            2: [Posicao(2, 0), Posicao(2, 1), Posicao(2, 2), Posicao(2, 3)],
            3: [Posicao(0, 1), Posicao(1, 1), Posicao(2, 1), Posicao(3, 1)]
        }
        self.move(-1, 3)

class BlocoO (Bloco):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [Posicao(0, 0), Posicao(0, 1), Posicao(1, 0), Posicao(1, 1)]
        }
        self.move(0, 4)

class BlocoS(Bloco):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Posicao(0,1), Posicao(0,2), Posicao(1,0), Posicao(1,1)],
            1: [Posicao(0,1), Posicao(1,1), Posicao(1,2), Posicao(2,2)],
            2: [Posicao(1,1), Posicao(1,2), Posicao(2,0), Posicao(2,1)],
            3: [Posicao(0,0), Posicao(1,0), Posicao(1,1), Posicao(2,1)]
        }
        self.move(0, 3)

class BlocoT(Bloco):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Posicao(0,1), Posicao(1,0), Posicao(1,1), Posicao(1,2)],
            1: [Posicao(0,1), Posicao(1,1), Posicao(1,2), Posicao(2,1)],
            2: [Posicao(1,0), Posicao(1,1), Posicao(1,2), Posicao(2,1)],
            3: [Posicao(0,1), Posicao(1,0), Posicao(1,1), Posicao(2,1)]
        }
        self.move(0, 3)

class BlocoZ(Bloco):
    def __init__(self):
        super().__init__(id=7)
        self.cells = {
            0: [Posicao(0,0), Posicao(0,1), Posicao(1,1), Posicao(1,2)],
            1: [Posicao(0,2), Posicao(1,1), Posicao(1,2), Posicao(2,1)],
            2: [Posicao(1,0), Posicao(1,1), Posicao(2,1), Posicao(2,2)],
            3: [Posicao(0,1), Posicao(1,0), Posicao(1,1), Posicao(2,0)]
        }
        self.move(0, 3)
