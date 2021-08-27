import pygame as pg
from Pokebola.Logica import LogicaInputs as LI
from Pokebola.Logica import LogicaMovimentacao as LM
from Pokebola.Logica import LogicaAnimacao as LA
from Pokebola.Dados import DadosPokebolaArremessavel as DP1

def AtualizarPokebolaArremessavel():
    if DP1.XPokebola >= 700 or DP1.XPokebola<=-35 or DP1.YPokebola>=630 or DP1.YPokebola<=-35:
        DP1.PokebolaMovendoDireita, DP1.PokebolaMovendoEsquerda, DP1.PokebolaMovendoAbaixo, DP1.PokebolaMovendoAcima = False, False, False, False
        DP1.Arremessada = False
    LI.LogicaInputsPokebola()
    LM.LogicaMovimentacaoPokebola()
    LA.LogicaAnimacaoPokebola()
    DP1.Pokebola.rect = pg.Rect(DP1.XPokebola, DP1.YPokebola, DP1.LarguraPokebola, DP1.AlturaPokebola)
