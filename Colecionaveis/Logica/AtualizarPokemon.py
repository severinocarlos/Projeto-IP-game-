import pygame as pg
from Colecionaveis.Logica import LogicaPokemon as LP
from Colecionaveis.Dados import DadosPokemon as DP
def AtualizarPokemon():
    LP.ColetarPokemon()
    DP.Pokemon.rect = pg.Rect(DP.XPokemon,DP.YPokemon,DP.LarguraPokemon,DP.AlturaPokemon)
    DP.Pokemon.image = pg.transform.scale(DP.Pokemon.image, [50, 50])
