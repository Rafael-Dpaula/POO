from status import Status

class Missao:
    def __init__(
        self, nome, descricao, recompensa: float, status = Status.PENDENTE
    ):
        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa
        self.status = status

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
            raise Exception("ERROR: o campo nome é obrigatório.")
        self.__nome: str = novoNome.title().strip()

    @descricao.setter
    def descricao(self, novoDesc: str):
        if novoDesc is None:
            raise Exception("ERROR: o campo descrição é obrigatório.")
        self.__descricao: str = novoDesc.strip()

    @recompensa.setter
    def recompensa(self, novaRecomp: float):
        if novaRecomp is None:
            raise Exception("ERROR: o campo recompensa é obrigatório.")
        elif novaRecomp > 50 or novaRecomp < 0 or not isinstance(novaRecomp, int):
            raise ValueError(
                "ERROR: o valor da recompensa deve ser um inteiro entre [0; 50]."
            )
        self.__recompensa: int = novaRecomp

    @status.setter
    def status(self, novoStatus: str):
        self.__status: str = novoStatus

    def exibir_dados(self):
        return f"{self.__class__.__name__}\nMISSÂO: \nNome: {self.nome}\nDescrição: {self.descricao}\nRecompensa: {self.recompensa} XP\nStatus: {self.status.value}\n"

    def __str__(self):
        return f"{self.__class__.__name__}\nMISSÂO: \nNome: {self.nome}\nDescrição: {self.descricao}\nRecompensa: {self.recompensa} XP\nStatus: {self.status.value}\n"

    def __eq__(self, object2):
        return self.recompensa == object2.recompensa

    def iniciar_missao(self):
        if self.status == Status.PENDENTE:
            self.status = Status.EM_ANDAMENTO
            return f"A missão {self.nome} começou! Objetivo central da missão: {self.descricao}\n"
        else:
            raise Exception("ERROR: o status da missão deve ser pendente!")
        
    def concluir_missao(self):
        if self.status == Status.EM_ANDAMENTO:
            self.status = Status.CONCLUIDA
            return f"Missão concluída com sucesso. A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira\n"
        else:
            raise Exception("ERROR: o status da missão deve estar em andamento!")



class MissaoCombate(Missao):
    def __init__(
        self,
        nome,
        descricao,
        recompensa: float,
        inimigo: str,
        inimigos_a_derrotar: int,
        status: str = Status.PENDENTE,
    ):
        super().__init__(nome, descricao, recompensa, status)
        self.inimigo = inimigo
        self.inimigo_a_derrotar = inimigos_a_derrotar

    @property
    def inimigo(self):
        return self.__inimigo

    @property
    def inimigos_a_derrotar(self):
        return self.__inimigos_a_derrotar

    @inimigo.setter
    def inimigo(self, novoInimigo):
        if novoInimigo == "":
            raise ValueError("ERROR: o campo inimigo é obrigatório.")
        self.__inimigo = novoInimigo

    @inimigos_a_derrotar.setter
    def inimigos_a_derrotar(self, novaDerrota):
        if novaDerrota <= 0:
            raise ValueError("ERROR: a quantidade de inimigos deve ser maior que 0.")

    def __str__(self):
        return (
            super().__str__()
            + f"Tipo inimigo: {self.inimigo}\nQuantidade de inimigos: {self.inimigo_a_derrotar}\n"
        )
    
    def concluir_missao(self, valor):
        if self.status == Status.EM_ANDAMENTO:
            if valor >= self.inimigo_a_derrotar:
                self.status = Status.CONCLUIDA
                return f"Missão concluída com sucesso. A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira\n"
            else:
                self.status = Status.FRACASSADA
                return f"A missão {self.nome} foi fracassada.\n"
        else:
            raise Exception("ERROR: o status da missão deve estar em andamento!")


class MissaoColeta(Missao):
    def __init__(
        self,
        nome,
        descricao,
        recompensa: int,
        item_necessario,
        quantidade_item: int,
        status: str = Status.PENDENTE,
    ):
        super().__init__(nome, descricao, recompensa, status)
        self.item_necessario = item_necessario
        self.quantidade_item = quantidade_item

    @property
    def item_necessario(self):
        return self.__item_necessario

    @property
    def quantidade_item(self):
        return self.__quantidade_item

    @item_necessario.setter
    def item_necessario(self, novoItem: str):
        if novoItem == "":
            raise ValueError("ERROR: o item necessário é obrigatório.")
        self.__item_necessario = novoItem

    @quantidade_item.setter
    def quantidade_item(self, novaQuantidade):
        if novaQuantidade <= 0:
            raise ValueError("ERROR: a quantidade deve ser maior que 0.")
        self.__quantidade_item = novaQuantidade

    def __str__(self):
        return (
            super().__str__()
            + f"Item necessário: {self.item_necessario}\nQuantidade necessária: {self.quantidade_item}\n"
        )

    def concluir_missao(self, valor):
        if self.status == Status.EM_ANDAMENTO:
            if valor >= self.quantidade_item:
                self.status = Status.CONCLUIDA
                return f"Missão concluída com sucesso. A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira\n"
            else:
                self.status = Status.FRACASSADA
                return f"A missão {self.nome} foi fracassada.\n"
        else:
            raise Exception("ERROR: o status da missão deve estar em andamento!")


class MissaoExploracao(Missao):
    def __init__(
        self,
        nome: str,
        descricao: str,
        recompensa: int,
        local: str,
        distancia: float,
        tempo_limite: int,
        status: str = Status.PENDENTE,
    ):
        super().__init__(nome, descricao, recompensa, status)
        self.local = local
        self.distancia = distancia
        self.tempo_limite = tempo_limite

    @property
    def local(self):
        return self.__local

    @property
    def distancia(self):
        return self.__distancia

    @property
    def tempo_limite(self):
        return self.__tempo_limite

    @local.setter
    def local(self, novoLocal: str):
        if novoLocal == "":
            raise ValueError("ERROR: o local é obrigatório")
        self.__local = novoLocal

    @distancia.setter
    def distancia(self, novaDistancia: float):
        if novaDistancia <= 0:
            raise ValueError("ERROR: a distancia deve ser maior que 0")
        self.__distancia = novaDistancia

    @tempo_limite.setter
    def tempo_limite(self, novoTempo: float):
        if novoTempo <= 0:
            raise ValueError("ERROR: o tempo limite deve ser maior que 0")
        self.__tempo_limite = novoTempo

    def __str__(self):
        return (
            super().__str__()
            + f"Local: {self.local}\nDistância (KM): {self.distancia}\nTempo limite: {self.tempo_limite}%\n"
        )

    def concluir_missao(self, valor):
        if self.status == Status.EM_ANDAMENTO:
            if valor >= self.distancia:
                self.status = Status.CONCLUIDA
                return f"Missão concluída com sucesso. A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira\n"
            else:
                self.status = Status.FRACASSADA
                return f"A missão {self.nome} foi fracassada.\n"
        else:
            raise Exception("ERROR: o status da missão deve estar em andamento!")
