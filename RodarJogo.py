import pygame as pg
pg.init()

from Janela.Dados import DadosJanela as DT
import Montador as M
from Janela.Dados import DadosTelaFinal as DTF

StartGame = False

def RodarJogo():
    global StartGame
    # Loop do Jogo
    while DT.JanelaAberta:
        if not StartGame:
            M.TelaInicial()
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    DT.JanelaAberta = False
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        StartGame = True
                    if evento.key == pg.K_ESCAPE:
                        DT.JanelaAberta = False
        if StartGame:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    DT.JanelaAberta = False
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_ESCAPE and StartGame:
                        DT.JanelaAberta = False
            if not DTF.TelaFinal:
                M.Montar()
            if DTF.TelaFinal:
                M.TelaFinal()
