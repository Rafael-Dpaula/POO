from personagem import Personagem
from missao import Missao, MissaoColeta, MissaoCombate, MissaoExploracao

personagem1 = Personagem("Zen")
personagem2 = Personagem("Mark")

print(personagem1)
print(personagem2)

Combate = MissaoCombate(
    nome="Extermínio Sombrio",
    descricao="Derrote criaturas corrompidas na floresta",
    recompensa=25,
    inimigo="Corrompido",
    inimigos_a_derrotar=5
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

print(Combate)
print(Combate.iniciar_missao())
print(Combate.concluir_missao(5))
print(Combate.exibir_dados())

print(Coleta)
print(Coleta.iniciar_missao())
print(Coleta.concluir_missao(9))
print(Coleta.exibir_dados())

print(Exploracao)
print(Exploracao.iniciar_missao())
print(Exploracao.concluir_missao(13))
print(Exploracao.exibir_dados())