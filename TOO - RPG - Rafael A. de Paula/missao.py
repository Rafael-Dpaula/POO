class Missao:
    def __init__(self, nome, descricao, recompensa: float, status: str = "Pendente"):
        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa
        self.status = status

    def _validar_status(self, status_input: str):
        status_map = {
            "pendente": "Pendente",
            "em andamento": "Em Andamento",
            "concluida": "Concluída"
        }
        if status_input in status_map:
            return status_map[status_input]
        raise ValueError(f"Status inválido: '{status_input}'. Use: Pendente, Em Andamento, Concluída")

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
        elif novaRecomp > 50 or novaRecomp < 0 or not isinstance(novaRecomp, int):
            raise ValueError("Valor da recompensa deve ser um inteiro entre [0; 50]")
        self.__recompensa = novaRecomp

    @status.setter
    def status(self, novoStatus):
        self.__status = self._validar_status(novoStatus.lower().strip())

    def exibir_dados(self):
        print(f"MISSÂO: \nNome: {self.nome}\nDescrição: {self.descricao}\nRecompensa: {self.recompensa}\nStatus: {self.status}\n")
        

    def __str__(self):
        return f"{self.nome} \n {self.descricao} \n {self.recompensa} \n {self.status}"

    def __eq__(self, object2):
        return self.recompensa == object2.recompensa