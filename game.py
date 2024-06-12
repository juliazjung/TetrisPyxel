import pyxel

from grid import Grid
from blocos import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocos = [BlocoI(), BlocoJ(), BlocoL(), BlocoO(), BlocoS(), BlocoT(), BlocoZ()]
        self.current_bloco = self.get_bloco_aleatorio()
        self.next_bloco = self.get_bloco_aleatorio()
        self.game_over = False
        self.score = 0
        self.nivel = 1

    def atualizar_nivel(self):
        if self.score > (750 * self.nivel) and self.score > 0:
            self.nivel += 1

    def atualizar_score(self, linhas_limpas, pontos_moverPraBaixo, espaco):
        if linhas_limpas == 1:
            self.score += 100
        elif linhas_limpas == 2:
            self.score += 300
        elif linhas_limpas >= 3:
            self.score += 500
        if espaco == True:
            self.score += 30
        self.score += pontos_moverPraBaixo

    def get_bloco_aleatorio(self):
        if len(self.blocos) == 0:
            self.blocos = [BlocoI(), BlocoJ(), BlocoL(), BlocoO(), BlocoS(), BlocoT(), BlocoZ()]
        bloco = random.choice(self.blocos)
        self.blocos.remove(bloco)
        return bloco

    def move_left(self):
        self.current_bloco.move(0, -1)
        if self.bloco_inside() == False or self.bloco_fits() == False:
            self.current_bloco.move(0, 1)

    def move_right(self):
        self.current_bloco.move(0, 1)
        if self.bloco_inside() == False or self.bloco_fits() == False:
            self.current_bloco.move(0, -1)

    def move_down(self):
        self.current_bloco.move(1, 0)
        if not self.bloco_inside() or not self.bloco_fits():
            self.current_bloco.move(-1, 0)
            self.lock_bloco()

    def lock_bloco(self):
        tiles = self.current_bloco.get_posicao_cell()
        for tile in tiles:
            self.grid.grid[tile.linha][tile.coluna] = self.current_bloco.id
        self.current_bloco = self.next_bloco
        self.next_bloco = self.get_bloco_aleatorio()
        linhas_limpas = self.grid.reprocessar_linhas()
        self.atualizar_score(linhas_limpas, 0, False)
        self.atualizar_nivel()
        if self.bloco_fits() == False:
            try:
                self.game_over = True
                self.grid = Grid()
                self.draw()
            except:
                pyxel.quit()

    def move_total(self, bloco):
        while self.bloco_fits() and self.current_bloco == bloco:
            self.move_down()

    def reset(self):
        self.score = 0
        self.nivel = 1
        self.grid.reset()
        self.blocos = [BlocoI(), BlocoJ(), BlocoL(), BlocoO(), BlocoS(), BlocoT(), BlocoZ()]
        self.current_bloco = self.get_bloco_aleatorio()
        self.next_bloco = self.get_bloco_aleatorio()

    def bloco_fits(self):
        tiles = self.current_bloco.get_posicao_cell()
        for tile in tiles:
            if not self.grid.is_empty(tile.linha, tile.coluna):
                return False
        return True

    def rotacao(self):
        self.current_bloco.rotacao()
        if self.bloco_inside() == False or self.bloco_fits() == False:
            self.current_bloco.desfaz_rotacao()

    def bloco_inside(self):
        tiles = self.current_bloco.get_posicao_cell()
        for tile in tiles:
            if self.grid.is_inside(tile.linha, tile.coluna) == False:
                return False
        return True

    def draw(self):
        self.grid.draw(11, 100)
        if self.game_over == False:
            try:
                self.current_bloco.draw(11, 100)
                self.next_bloco.draw(270, 370)
            except:
                print('Erro ao desenhar o jogo.')
