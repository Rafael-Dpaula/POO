class Personagem:
    def __init__(self, nome, nivel = 1, xp = 0, vida = 100):
        self.nome = nome
        self.nivel = nivel
        self.xp = xp
        self.vida = vida
    
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
    
    @nome.setter
    def nome(self, novoNome: str):
        if novoNome is None:
            raise Exception("Nome é obrigatório.")
        self.__nome = novoNome.title().strip()

    @nivel.setter
    def nivel(self, novoNivel: int):
        if novoNivel < 0:
            raise Exception("Nível inválido.")
        self.__nivel = novoNivel

    @xp.setter
    def xp(self, novoXp: str):
        if novoXp < 0:
            raise Exception("Experiência inválida.")
        self.__xp = novoXp

    @vida.setter
    def vida(self, novoVida: str):
        if novoVida < 0 or novoVida > 100:
            raise Exception("Vida inválida.")
        self.__vida = novoVida
    
    def __str__(self):
        return f"PERSONAGEM: \n\nNome: {self.nome}\nNível: {self.nivel}\nExperiência: {self.xp}\nPontos de vida: {self.vida}"