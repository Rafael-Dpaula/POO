from abc import ABC, abstractmethod


class EstadoMissao(ABC):
    def __init__(self, missao):
        self.missao = missao

    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def concluir(self, valor):
        pass


class EstadoPendente(EstadoMissao):
    def iniciar(self):
        self.missao.estado = EstadoAndamento(self.missao)
        return (
            f"A missão {self.missao.nome} começou! "
            f"Objetivo central da missão: {self.missao.descricao}\n"
        )

    def concluir(self, valor):
        raise Exception("ERROR: o status da missão deve ser pendente para iniciar!")


class EstadoAndamento(EstadoMissao):
    def iniciar(self):
        raise Exception("ERROR: a missão já está em andamento!")

    def concluir(self, valor):
        # Delegar a lógica específica (tipo da missão) para a própria missão
        return self.missao.concluirAndamento(valor)


class EstadoConcluida(EstadoMissao):
    def iniciar(self):
        raise Exception("ERROR: a missão já está concluída!")

    def concluir(self, valor):
        raise Exception("ERROR: a missão já está concluída!")


class EstadoFracassada(EstadoMissao):
    def iniciar(self):
        raise Exception("ERROR: a missão fracassou!")

    def concluir(self, valor):
        raise Exception("ERROR: a missão fracassou!")
