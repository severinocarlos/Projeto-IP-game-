import pygame as pg
import time
from Janela.Logica import LogicaTela as LT
from Jogador.Logica import AtualizarJogador as AJ
from Inimigo.Logica import AtualizarInimigo as AI
from HUD.Logica import LogicaContador as LC
from Colecionaveis.Logica import AtualizarPokebola as AP1
from Colecionaveis.Logica import AtualizarPokemon as AP2
from Pokebola.Logica import AtualizarPokebolaArremessavel as APb

def AtualizarJanela():
    LT.CarregarMapa()
    LT.CarregarPokebolaColecionavel()
    LT.CarregarPokemonColecionavel()
    LT.CarregarInimigo()
    LT.CarregarJogador()
    LT.CarregarPokebolaArremessavel()
    LT.CarregarHUD()
    pg.display.update()

def Montar():
    TempoInicio = time.time()
    #from NovoSistemaArquitetado.Sons.Logica import LogicaMusica
    AJ.AtualizarJogador()
    AI.AtualizarInimigo()
    AP1.AtualizarPokebola()
    AP2.AtualizarPokemon()
    APb.AtualizarPokebolaArremessavel()
    AtualizarJanela()
    TempoAposExecucao = time.time()
    TempoDeEspera = (1 - (TempoAposExecucao - TempoInicio)) / 180
    time.sleep(TempoDeEspera)
    TempoAposSleep = time.time()
    LC.Contador(TempoInicio,TempoAposSleep)

def TelaInicial():
    LT.CarregarTelaInicial()
    pg.display.update()

def TelaFinal():
    LT.CarregarTelaFinal()
    pg.display.update()
