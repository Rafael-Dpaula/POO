from models.missao import *

class FactoryMissao():
    @staticmethod
    def criarMissao(tipo_missao: str, nome, descricao, recompensa, valor_str: str, valor_num):
        tipo_missao = tipo_missao.strip().lower()

        if(tipo_missao == "combate"):
            missaoNova = MissaoCombate(nome, descricao, recompensa, valor_str, valor_num)
        elif(tipo_missao == "coleta"):
            missaoNova = MissaoColeta(nome, descricao, recompensa, valor_str, valor_num)
        elif(tipo_missao == "exploracao"):
            missaoNova = MissaoExploracao(nome, descricao, recompensa, valor_str, valor_num)
        else:
            return Exception("Tipo da Missão Inválida.")
        return missaoNova