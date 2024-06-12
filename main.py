import pyxel
from game import Game

pyxel.init(500, 720, fps=60)
cor = 7

game = Game()

def update():
    if pyxel.btnp(pyxel.KEY_ESCAPE):
        pyxel.quit()

    if not game.game_over:
        if pyxel.btnp(pyxel.KEY_LEFT):
            game.move_left()

        if pyxel.btnp(pyxel.KEY_RIGHT):
            game.move_right()

        if pyxel.btnp(pyxel.KEY_DOWN):
            game.move_down()
            game.atualizar_score(0, 1, False)

        if pyxel.btnp(pyxel.KEY_DOWN, 7, 7):
            game.move_down()
            game.atualizar_score(0, 1, False)

        if pyxel.btnp(pyxel.KEY_UP):
            game.rotacao()

        if pyxel.btnp(pyxel.KEY_SPACE, 20, 20):
            game.move_total(game.current_bloco)
            game.atualizar_score(0, 0, True)

        try:
            if pyxel.frame_count % int(50 / game.nivel) == 0:
                game.move_down()
        except:
            pass

    if pyxel.btnp(pyxel.KEY_SPACE) and game.game_over == True:
        game.game_over = False
        game.reset()

def draw():
    try:
        pyxel.cls(1)
        game.draw()
        msg = 'SCORE'
        pyxel.text(150, 55, msg, cor)
        pyxel.text(150, 70, str(game.score), cor)
        msg = 'PROXIMO BLOCO'
        pyxel.text(380, 330, msg, cor)
        msg = 'NIVEL'
        pyxel.text(400, 200, msg, cor)
        pyxel.text(410, 220, str(game.nivel), cor)
    except:
        pyxel.quit()

pyxel.run(update, draw)
