from personagem import Personagem
from missao import Missao

missao1 = Missao("Caça à monstros", "Encontre e elimine os monstros.", 15)
missao2 = Missao("Coleta", "Encontre materiais.", 3, "em andamento")

personagem1 = Personagem("Zen")
personagem2 = Personagem("Mark")

#print(personagem1, "\n\n", missao2, "\n\n", personagem2, "\n\n", missao1)
personagem1.exibir_dados()
personagem2.exibir_dados()
missao1.exibir_dados()
missao2.exibir_dados()

if missao1.__eq__(missao2):
    print(f"A missão de {missao1.nome}, tem a mesma recompensa que a missão {missao2.nome}")
else:
    print(f"A missão de {missao1.nome}, NÃO tem a mesma recompensa que a missão {missao2.nome}")
    
if personagem1.__eq__(personagem2):
    print(f"O personagem {personagem1.nome}, tem o mesmo nível que o personagem {personagem2.nome}")
else:
    print(f"O personagem {personagem1.nome}, NÃO tem o mesmo nível que o personagem {personagem2.nome}")
    