from status import Status
class Personagem:
    def __init__(self, nome, nivel = 1, xp = 0, vida = 100, missoes = []):
        if not isinstance(nivel, int):
            raise Exception("Nível deve ser inteiro.")
        if not isinstance(xp, int):
            raise Exception("XP deve ser inteiro.")
        if not isinstance(vida, int):
            raise Exception("Vida deve ser inteiro.")
        
        self.nome = nome
        self.__nivel = nivel
        self.__xp = xp
        self.__vida = vida
        self.__missoes = list(missoes)
        
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def nivel(self):
        return self.__nivel
    
    @property
    def xp(self):
        return self.__xp
    
    @property
    def vida(self):
        return self.__vida
    
    @property
    def missoes(self):
        return self.__missoes
    
    @nome.setter
    def nome(self, novoNome: str):
        if novoNome is None:
            raise Exception("Nome é obrigatório.")
        self.__nome = novoNome.title().strip()

    def exibir_dados(self):
        print(f"PERSONAGEM: \nNome: {self.__nome}\nNível: {self.__nivel}\nExperiência: {self.__xp}\nPontos de vida: {self.__vida}\nMissões: {[m.nome for m in self.__missoes]}\n")
        
    
    def __str__(self):
        return f"PERSONAGEM: \nNome: {self.__nome}\nNível: {self.__nivel}\nExperiência: {self.__xp}\nPontos de vida: {self.__vida}\nMissões: {[m.nome for m in self.__missoes]}\n"
    
    def __eq__(self, object2):
        return self.nivel == object2.nivel
    
    def add_missao(self, missao):
        if not any(m.nome == missao.nome for m in self.__missoes):
            self.__missoes.append(missao)
            missao.iniciar_missao()
            return f"A missão {missao.nome} foi adicionada a lista de missões de {self.__nome}.\n"
        return f"A missão {missao.nome} JÁ ESTÁ na lista de missões de {self.__nome}.\n"

    def concluir_missao(self, missao, valor):
        if any(m.nome == missao.nome for m in self.__missoes):
            resultado = missao.concluir_missao(valor)
            subiu = ""
            if missao.status == Status.CONCLUIDA:
                self.__xp += missao.recompensa
                if self.__xp >= 100:
                    while self.__xp >= 100:
                        self.__xp -= 100
                        self.__nivel += 1
                        subiu = (f"\nO personagem {self.__nome} subíu para o nível {self.__nivel}\n")
                self.__missoes.remove(missao)
                return f"{missao.nome}: {resultado}{subiu}"
            else:
                return f"{missao.nome}: {resultado}"
        else:
            return f"{missao.nome}: A missao '{missao.nome}' não foi encontrada no personagem {self.__nome}\n"

