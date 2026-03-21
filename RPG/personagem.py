class Personagem:
    def __init__(self, nome, nivel = 1, xp = 0, vida = 100):
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

    def exibir_dados(self):
        print(f"PERSONAGEM: \nNome: {self.nome}\nNível: {self.nivel}\nExperiência: {self.xp}\nPontos de vida: {self.vida}\n")
        
    
    def __str__(self):
        return f"PERSONAGEM: \n {self.nome} \n {self.nivel} \n {self.xp} \n {self.vida}"
    
    def __eq__(self, object2):
        return self.nivel == object2.nivel
