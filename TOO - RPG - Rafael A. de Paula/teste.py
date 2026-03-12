from personagem import Personagem
from missao import Missao

missao1 = Missao("Caça à monstros", "Encontre e elimine os monstros.", 15, False)
missao2 = Missao("Coleta", "Encontre materiais.", 3, True)

personagem1 = Personagem("Zen", 37, 230)
personagem2 = Personagem("Mark")

print(personagem1, "\n\n", missao2, "\n\n", personagem2, "\n\n", missao1)