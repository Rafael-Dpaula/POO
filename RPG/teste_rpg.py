from personagem import Personagem
from missao import MissaoColeta, MissaoCombate, MissaoExploracao
from item import Item, TipoItem

#instanciamento de Personagens
personagem1 = Personagem("Zen")
personagem2 = Personagem("Mark")

#instanciamento de missoes
Combate = MissaoCombate(
    nome="Extermínio Sombrio",
    descricao="Derrote criaturas corrompidas na floresta",
    recompensa=50,
    inimigo="Corrompido",
    inimigos_a_derrotar=5,
)

Combate2 = MissaoCombate(
    nome="Limpar a dungeon norte",
    descricao="Derrote todos as criaturas presentes no 1º andar da dungeon norte",
    recompensa=50,
    inimigo="Goblins",
    inimigos_a_derrotar=18,
)

Exploracao = MissaoExploracao(
    nome="Explorador de Arcadia",
    descricao="Explore a região esquecida ao norte",
    recompensa=30,
    local="Ruínas Antigas",
    distancia=12.5,
)

Coleta = MissaoColeta(
    nome="Coleta de Ervas",
    descricao="Colete ervas medicinais raras",
    recompensa=15,
    item_necessario="Erva Lunar",
    quantidade_item=10,
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
