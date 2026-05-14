# adiciona o diretório raiz ao sys.path para garantir que os módulos sejam encontrados
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.personagem import Personagem
from models.missao import *
from models.factoryMissao import FactoryMissao
from models.item import Item, TipoItem

#instanciamento de Personagens
personagem1 = Personagem("Zen")
personagem2 = Personagem("Mark")

#instanciamento de missoes
Combate = FactoryMissao.criarMissao(
    tipo_missao="combate",
    nome="Extermínio Sombrio",
    descricao="Derrote criaturas corrompidas na floresta",
    recompensa=50,
    valor_str="Corrompido",
    valor_num=5,
)

Combate2 = FactoryMissao.criarMissao(
    tipo_missao="combate",
    nome="Limpar a dungeon norte",
    descricao="Derrote todos as criaturas presentes no 1º andar da dungeon norte",
    recompensa=50,
    valor_str="Goblins",
    valor_num=18,
)

Exploracao = FactoryMissao.criarMissao(
    tipo_missao="exploracao",
    nome="Explorador de Arcadia",
    descricao="Explore a região esquecida ao norte",
    recompensa=30,
    valor_str="Ruínas Antigas",
    valor_num=12.5,
)

Coleta = FactoryMissao.criarMissao(
    tipo_missao="coleta",
    nome="Coleta de Ervas",
    descricao="Colete ervas medicinais raras",
    recompensa=15,
    valor_str="Erva Lunar",
    valor_num=10,
)

#instanciamento de Itens
espada_ferro = Item(
    "Espada de Ferro Rúnico",
    "Uma lâmina antiga com inscrições mágicas desgastadas.",
    15,
    TipoItem.ARMA,
)

arco_silvestre = Item(
    "Arco Silvestre", "Feito de madeira élfica, leve e preciso.", 12, TipoItem.ARMA
)

armadura_couro = Item(
    "Armadura de Couro Endurecido",
    "Proteção básica usada por aventureiros iniciantes.",
    8,
    TipoItem.VESTIMENTA,
)

capa_sombria = Item(
    "Capa Sombria", "Dificulta ser detectado em áreas escuras.", 5, TipoItem.VESTIMENTA
)

pocao_vida = Item(
    "Poção de Vida",
    "Restaura pontos de vida ao ser consumida.",
    20,
    TipoItem.UTILITARIO,
)

bomba_fumaca = Item(
    "Bomba de Fumaça",
    "Permite escapar rapidamente de combates.",
    0,
    TipoItem.UTILITARIO,
)

#listagem de personagens
print(personagem1)

#listagem da missao
print(Exploracao)

#adicionando missao teste sem itens equipados
personagem1.add_missao(Exploracao)

#adicionando itens ao personagen
personagem1.add_Item(bomba_fumaca)
personagem1.add_Item(capa_sombria)
personagem1.add_Item(arco_silvestre)

#mostrando o inventario do personagem
personagem1.mostrar_Inventario()

#testando equipar item que não está no inventário do personagem
personagem1.equiparItens(espada_ferro, capa_sombria, bomba_fumaca)

#mostrando personagem
print(personagem1)

#equipando todos os itens no personagem
personagem1.equiparItens(arco_silvestre, capa_sombria, bomba_fumaca)

#adicionando a missao
personagem1.add_missao(Exploracao)

#mostrando personagem
personagem1.exibir_dados()

#Substituindo arma
personagem1.add_Item(espada_ferro)
personagem1.equiparItens(espada_ferro, capa_sombria, bomba_fumaca)

#mostrando personagem
personagem1.exibir_dados()
