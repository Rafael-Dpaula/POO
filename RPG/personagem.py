from status import Status
class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.__nivel = 1
        self.__xp = 0
        self.__vida = 100
        self.__missoes = []
        self.__ataque = 0
        self.__inventario = []
        
    
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
    
    @property
    def inventario(self):
        return self.__inventario
    
    @property
    def ataque(self):
        return self.__ataque
    
    @nome.setter
    def nome(self, novoNome: str):
        if novoNome is None:
            raise Exception("Nome é obrigatório.")
        self.__nome = novoNome.title().strip()

    def exibir_dados(self):
        print(f"------ PERSONAGEM ------ \nNome: {self.__nome}\nNível: {self.__nivel}\nExperiência: {self.__xp}\nPontos de vida: {self.__vida}\nMissões: {[m.nome for m in self.__missoes]}\n")
        
    
    def __str__(self):
        return f"------ PERSONAGEM ------ \nNome: {self.__nome}\nNível: {self.__nivel}\nExperiência: {self.__xp}\nPontos de vida: {self.__vida}\nMissões: {[m.nome for m in self.__missoes]}\n"
    
    def __eq__(self, object2):
        return self.nivel == object2.nivel
    
    def add_missao(self, missao):
        if not any(m.nome == missao.nome for m in self.__missoes):
            self.__missoes.append(missao)
            missao.iniciar_missao()
            return f"------ Missão Colocada na Lista ------\nA missão {missao.nome} foi adicionada a lista de missões de {self.__nome}.\n"
        return f"------ Falha em Colocar Missão na Lista ------\nA missão {missao.nome} JÁ ESTÁ na lista de missões de {self.__nome}.\n"

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
                        subiu = (f"\n------ SUBIDA DE NÍVEL ------\nO personagem {self.__nome} subíu para o nível {self.__nivel}\n")
                self.__missoes.remove(missao)
                return f"{resultado}{subiu}"
            else:
                self.__missoes.remove(missao)
                self.__vida -= 10
                return f"{resultado}"
        else:
            return f"------ Falha na Conclusão de Missão ------\n{missao.nome}: A missao '{missao.nome}' não foi encontrada no personagem {self.__nome}\n"

