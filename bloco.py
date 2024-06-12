from cores import Cores
from posicao import Posicao
import pyxel

class Bloco:
    def __init__ (self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.linha_offset = 0
        self.col_offset = 0
        self.estado_rotacao = 0
        cores = Cores()
        self.colors = cores.get_colors()

    def move(self, linha, coluna):
        self.linha_offset += linha
        self.col_offset += coluna

    def get_posicao_cell(self):
        tiles = self.cells[self.estado_rotacao]
        moved_tiles = []
        for posicao in tiles:
            posicao = Posicao(posicao.linha + self.linha_offset, posicao.coluna + self.col_offset)
            moved_tiles.append(posicao)

        return moved_tiles

    def rotacao(self):
        self.estado_rotacao += 1
        if self.estado_rotacao == len(self.cells):
            self.estado_rotacao = 0

    def desfaz_rotacao(self):
        self.estado_rotacao -= 1
        if self.estado_rotacao == 0:
            self.estado_rotacao = len(self.cells) - 1

    def draw(self, offset_x, offset_y):
        tiles = self.get_posicao_cell()
        for tile in tiles:
            try:
                pyxel.rect(tile.coluna * self.cell_size + offset_x, tile.linha * self.cell_size + offset_y,
                       self.cell_size -1, self.cell_size -1, self.colors[self.id])
            except:
                print('Erro ao desenhar o bloco.')
