class Missao:
    def __init__(self, nome, descricao, recompensa: float, status: bool = False):
        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa
        self.status = "Pendente" if status else "Em Andamento"

    
    @property
    def nome(self):
        return self.__nome
    @property
    def descricao(self):
        return self.__descricao
    @property
    def recompensa(self):
        return self.__recompensa
    @property
    def status(self):
        return self.__status
    
    @nome.setter
    def nome(self, novoNome: str):
        if novoNome is None:
            raise Exception("Nome é obrigatório.")
        self.__nome = novoNome.title().strip()
    
    @descricao.setter
    def descricao(self, novoDesc: str):
        if novoDesc is None:
            raise Exception("Descrição é obrigatório.")
        self.__descricao = novoDesc.strip()

    @recompensa.setter
    def recompensa(self, novaRecomp: float):
        if novaRecomp is None:
            raise Exception("Recompensa é obrigatório.")
        self.__recompensa = novaRecomp

    @status.setter
    def status(self, novoStatus):
        self.__status = novoStatus

    def __str__(self):
        return f"MISSÂO: \n\nNome: {self.nome}\nDescrição: {self.descricao}\nRecompensa: {self.recompensa}\nStatus: {self.status}"