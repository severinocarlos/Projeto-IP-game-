import pygame as pg
import random

LarguraPokebola,AlturaPokebola = 35,35
XPokebola,YPokebola = random.randrange(0,666,35),random.randrange(0,596,35)

GrupoPokebola = pg.sprite.Group()
Pokebola = pg.sprite.Sprite(GrupoPokebola)
Pokebola.image = pg.image.load('Colecionaveis/Recursos/Pokebola.png')
Pokebola.image = pg.transform.scale(Pokebola.image, [35,35])
Pokebola.rect = pg.Rect(XPokebola,YPokebola,LarguraPokebola,AlturaPokebola)