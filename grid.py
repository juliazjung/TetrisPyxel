import pyxel
from cores import Cores

class Grid:
    def __init__ (self):
        self.grid_linhas = 20
        self.grid_colunas = 10
        self.grid_size = 30
        self.grid = [[0 for j in range(self.grid_colunas)] for i in range(self.grid_linhas)]
        cores = Cores()
        self.colors = cores.get_colors()

    def printGrid(self):
        for lin in range(self.grid_linhas):
            for col in range(self.grid_colunas):
                print(self.grid[lin][col], end = " ")
            print()

    def is_inside(self, linha, coluna):
        if linha >= 0 and linha < self.grid_linhas and coluna >= 0 and coluna < self.grid_colunas:
            return True
        return False

    def is_empty(self, linha, coluna):
        if self.grid[linha][coluna] == 0:
            return True
        return False

    def is_linha_completa(self, linha):
        for coluna in range(self.grid_colunas):
            if self.grid[linha][coluna] == 0:
                return False
        return True

    def limpar_linha(self, linha):
        for coluna in range(self.grid_colunas):
            self.grid[linha][coluna] = 0

    def mover_linha_abaixo(self, linha, num_linhas):
        for coluna in range(self.grid_colunas):
            self.grid[linha+num_linhas][coluna] = self.grid[linha][coluna]
            self.grid[linha][coluna] = 0

    def reprocessar_linhas(self):
        completa = 0
        for linha in range(self.grid_linhas-1, 0, -1):
            if self.is_linha_completa(linha):
                self.limpar_linha(linha)
                completa += 1
            elif completa > 0:
                self.mover_linha_abaixo(linha, completa)
        return completa

    def reset(self):
        for linha in range(self.grid_linhas):
            for coluna in range(self.grid_colunas):
                self.grid[linha][coluna] = 0

    def draw(self, offset_x, offset_y):
        for lin in range(self.grid_linhas):
            for col in range(self.grid_colunas):
                try:
                    cell_valor = self.grid[lin][col]
                    pyxel.rect(col*self.grid_size + offset_x, lin*self.grid_size + offset_y,
                            self.grid_size -1, self.grid_size -1, self.colors[cell_valor])
                except:
                    print('Erro ao desenhar a grid.')
