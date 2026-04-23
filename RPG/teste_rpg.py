from personagem import Personagem
from missao import MissaoColeta, MissaoCombate, MissaoExploracao

personagem1 = Personagem("Zen")
personagem2 = Personagem("Mark")


Combate = MissaoCombate(
    nome="Extermínio Sombrio",
    descricao="Derrote criaturas corrompidas na floresta",
    recompensa=50,
    inimigo="Corrompido",
    inimigos_a_derrotar=5
)

Combate2 = MissaoCombate(
    nome = "Limpar a dungeon norte",
    descricao="Derrote todos as criaturas presentes no 1º andar da dungeon norte",
    recompensa=50,
    inimigo="Goblins",
    inimigos_a_derrotar=18
)

Exploracao = MissaoExploracao(
    nome="Explorador de Arcadia",
    descricao="Explore a região esquecida ao norte",
    recompensa=30,
    local="Ruínas Antigas",
    distancia=12.5,
    tempo_limite=60
)

Coleta = MissaoColeta(
    nome="Coleta de Ervas",
    descricao="Colete ervas medicinais raras",
    recompensa=15,
    item_necessario="Erva Lunar",
    quantidade_item=10
)
#testando listagem
print(Combate)
print(personagem1.add_missao(Combate))

#testando mudaça de status
print(Combate2)

#adicionando mais na lista
print(personagem1.add_missao(Combate2))

#testando a adicionar 2 vez o mesmo
print(personagem1.add_missao(Combate))

#adicionando mais missoes
print(personagem2.add_missao(Coleta))
print(personagem1.add_missao(Exploracao))

#testando se listou corretamente
print(personagem1)
print(personagem2)

#teste de concusão e remoção da missao
print(personagem1.concluir_missao(Combate, 5))
print(Combate)
print(personagem1)

#teste de subida de nível
print(personagem1.concluir_missao(Combate2, 20))

#teste de aumento de xp
print(personagem2.concluir_missao(Coleta, 8))
print(personagem2.concluir_missao(Combate, 5))

#exibição do personagem
personagem1.exibir_dados()
personagem2.exibir_dados()
