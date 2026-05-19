from abc import ABC, abstractmethod

from models.status import EstadoConcluida, EstadoFracassada, EstadoPendente


class Missao(ABC):
    def __init__(self, nome, descricao, recompensa: float):
        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa
        self.estado = EstadoPendente(self)

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
    def estado_atual(self):
        return self.estado

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

    def exibir_dados(self):
        return (
            f"------ {self.__class__.__name__} ------\n"
            f"MISSÃO: \n"
            f"Nome: {self.nome}\n"
            f"Descrição: {self.descricao}\n"
            f"Recompensa: {self.recompensa} XP\n"
            f"Status: {type(self.estado).__name__}\n"
        )

    def __str__(self):
        return (
            f"------ {self.__class__.__name__} ------\n"
            f"MISSÃO: \n"
            f"Nome: {self.nome}\n"
            f"Descrição: {self.descricao}\n"
            f"Recompensa: {self.recompensa} XP\n"
            f"Status: {type(self.estado).__name__}\n"
        )

    def __eq__(self, object2):
        if not isinstance(object2, Missao):
            return False
        return (
            self.nome == object2.nome
            and self.descricao == object2.descricao
            and self.recompensa == object2.recompensa
        )

    def iniciar_missao(self):
        return self.estado.iniciar()

    def concluir_missao(self, valor):
        return self.estado.concluir(valor)

    @abstractmethod
    def concluirAndamento(self, valor):
        pass


class MissaoCombate(Missao):
    def __init__(
        self,
        nome,
        descricao,
        recompensa: float,
        inimigo: str,
        inimigos_a_derrotar: int,
    ):
        super().__init__(nome, descricao, recompensa)
        self.inimigo = inimigo
        self.inimigos_a_derrotar = inimigos_a_derrotar

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
        self.__inimigos_a_derrotar = novaDerrota

    def __str__(self):
        return (
            super().__str__()
            + f"Tipo inimigo: {self.inimigo}\nQuantidade de inimigos: {self.inimigos_a_derrotar}\n"
        )

    def concluirAndamento(self, valor):
        if valor >= self.inimigos_a_derrotar:
            self.estado = EstadoConcluida(self)
            return (
                f"------ Conclusão de Missão ------\n"
                f"Missão '{self.nome}' concluída com sucesso. "
                f"A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira\n"
            )

        self.estado = EstadoFracassada(self)
        return (
            f"------ Missão Fracassada ------\nA missão '{self.nome}' foi fracassada.\n"
        )


class MissaoColeta(Missao):
    def __init__(
        self,
        nome,
        descricao,
        recompensa: int,
        item_necessario,
        quantidade_item: int,
    ):
        super().__init__(nome, descricao, recompensa)
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

    def concluirAndamento(self, valor):
        if valor >= self.quantidade_item:
            self.estado = EstadoConcluida(self)
            return (
                f"------ Conclusão de Missão ------\n"
                f"Missão '{self.nome}' concluída com sucesso. "
                f"A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira\n"
            )

        self.estado = EstadoFracassada(self)
        return (
            f"------ Missão Fracassada ------\nA missão '{self.nome}' foi fracassada.\n"
        )


class MissaoExploracao(Missao):
    def __init__(
        self,
        nome: str,
        descricao: str,
        recompensa: int,
        local: str,
        distancia: float,
    ):
        super().__init__(nome, descricao, recompensa)
        self.local = local
        self.distancia = distancia

    @property
    def local(self):
        return self.__local

    @property
    def distancia(self):
        return self.__distancia

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

    def __str__(self):
        return (
            super().__str__()
            + f"Local: {self.local}\nDistância (KM): {self.distancia}\n"
        )

    def concluirAndamento(self, valor):
        if valor >= self.distancia:
            self.estado = EstadoConcluida(self)
            return (
                f"------ Conclusão de Missão ------\n"
                f"Missão '{self.nome}' concluída com sucesso. "
                f"A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira\n"
            )

        self.estado = EstadoFracassada(self)
        return (
            f"------ Missão Fracassada ------\nA missão '{self.nome}' foi fracassada.\n"
        )
