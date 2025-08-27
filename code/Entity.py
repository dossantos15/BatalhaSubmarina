from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_VIDA, ENTITY_DANO, ENTITY_PONTO


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.vida = ENTITY_VIDA[self.name]
        self.dano = ENTITY_DANO[self.name]
        self.ponto = ENTITY_PONTO[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        pass