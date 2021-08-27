import pygame as pg
from Jogador.Logica import LogicaInputs as LI
from Jogador.Logica import LogicaMovimentacao as LM
from Jogador.Logica import LogicaAnimacao as LA
from Jogador.Dados import DadosJogador as DJ

def AtualizarJogador():
    if DJ.QuantidadePassos == 10:
        DJ.JogadorMovendoDireita, DJ.JogadorMovendoEsquerda, DJ.JogadorMovendoAbaixo, DJ.JogadorMovendoAcima = False, False, False, False
        DJ.Movendo = False
        DJ.QuantidadePassos = 0
    LI.LogicaInputsJogador()
    LM.LogicaMovimentacaoJogador()
    LA.LogicaAnimacaoJogador()
    DJ.Jogador.rect = pg.Rect(DJ.XJogador, DJ.YJogador, DJ.LarguraJogador, DJ.AlturaJogador)
