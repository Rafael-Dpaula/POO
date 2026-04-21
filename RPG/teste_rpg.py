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

print(personagem1.add_missao(Combate))
print(personagem1.add_missao(Combate2))
print(personagem1.add_missao(Combate))
print(personagem2.add_missao(Coleta))
print(personagem1.add_missao(Exploracao))

print(personagem1)
print(personagem2)

print(personagem1.concluir_missao(Combate, 5))
print(personagem1)
print(personagem1.concluir_missao(Combate2, 20))
print(personagem2.concluir_missao(Coleta, 8))
print(personagem2.concluir_missao(Combate, 5))

personagem1.exibir_dados()
personagem2.exibir_dados()
