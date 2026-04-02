from enum import Enum

class Status(Enum):
    PENDENTE = "PENDENTE"
    EM_ANDAMENTO = "EM ANDAMENTO"
    CONCLUIDA = "CONCLUÍDA"
    FRACASSADA = "FRACASSADA"