import random

from code.Fundo import Fundo
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Inimigo import Inimigo
from code.Jogador import Jogador


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Nivel1Bg':
                list_bg = []
                for i in range(6):
                    list_bg.append(Fundo(f'Nivel1Bg{i}', (0, 0)))
                    list_bg.append(Fundo(f'Nivel1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Nivel2Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Fundo(f'Nivel2Bg{i}', (0, 0)))
                    list_bg.append(Fundo(f'Nivel2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Jogador1':
                return Jogador('Jogador1', (10, WIN_HEIGHT / 2 - 30))
            case 'Jogador2':
                return Jogador('Jogador2', (10, WIN_HEIGHT / 2 + 30))
            case 'Inimigo1':
                return Inimigo('Inimigo1', (WIN_WIDTH + 10, random.randint(70, WIN_HEIGHT - 70)))
            case 'Inimigo2':
                return Inimigo('Inimigo2', (WIN_WIDTH + 10, random.randint(70, WIN_HEIGHT - 70)))