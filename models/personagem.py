from models.status import Status
from models.tipo_item import TipoItem
class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.__nivel = 1
        self.__xp = 0
        self.__vida = 20
        self.__missoes = []
        self.__ataqueBase = 10
        self.__inventario = []
        self.__arma = None
        self.__utilitario = None
        self.__vestimenta = None

        self.vidaBase = 20 #atributo que garante que buff de vida não seja cumulativo
        self.ataque = 10 #atributo que garante que buff de ataque não seja cumulativo
    
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
    def arma(self):
        return self.__arma
    
    @property
    def vestimenta(self):
        return self.__vestimenta
    
    @property
    def utilitario(self):
        return self.__utilitario
    
    @property
    def ataqueBase(self):
        return self.__ataqueBase
    
    @nome.setter
    def nome(self, novoNome: str):
        if novoNome is None:
            raise Exception("Nome é obrigatório.")
        self.__nome = novoNome.title().strip()

    def exibir_dados(self):
        print(f"------ PERSONAGEM ------ \nNome: {self.__nome}\nNível: {self.__nivel}\nExperiência: {self.__xp}\nPontos de vida: {self.__vida}\nAtaque base: {self.__ataqueBase}\nArma: {"Desarmado" if self.__arma is None else self.__arma.nome}\nVestimenta: {"Sem vestimenta" if self.__vestimenta is None else self.__vestimenta.nome}\nUtilitário: {"Sem utilitário" if self.__utilitario is None else self.__utilitario.nome}\nMissões: {[m.nome for m in self.__missoes]}\n")
        
    
    def __str__(self):
        return f"------ PERSONAGEM ------ \nNome: {self.__nome}\nNível: {self.__nivel}\nExperiência: {self.__xp}\nPontos de vida: {self.__vida}\nAtaque base: {self.__ataqueBase}\nArma: {"Desarmado" if self.__arma is None else self.__arma.nome}\nVestimenta: {"Sem vestimenta" if self.__vestimenta is None else self.__vestimenta.nome}\nUtilitário: {"Sem utilitário" if self.__utilitario is None else self.__utilitario.nome}\nMissões: {[m.nome for m in self.__missoes]}\n"
    
    def __eq__(self, object2):
        return self.nivel == object2.nivel
    
    def add_missao(self, missao):
        if self.__arma is None or self.__vestimenta is None or self.__utilitario is None:
            print(f"O jogador '{self.nome}' deve se equipar antes de aceitar uma missão.")
            return
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
        
    def equiparItens(self, arma, vestimenta, utilitario):
        efeitoVida = 0
        efeitoDano = 0
        if any(a.nome == arma.nome and a.tipo == TipoItem.ARMA for a in self.__inventario):
            self.__arma = arma
            print(f"A arma '{arma.nome}' foi equipada em {self.nome}")
            efeitoDano += arma.valorEfeito
        else:
            print(f"ERROR: o jogador '{self.nome}', não possui a arma equipada no inventário.")
        if any(u.nome == utilitario.nome and u.tipo == TipoItem.UTILITARIO for u in self.__inventario):
            self.__utilitario = utilitario
            print(f"O utilitário '{utilitario.nome}' foi equipado em {self.nome}")
            efeitoVida+= utilitario.valorEfeito
        else:
            print(f"ERROR: o jogador '{self.nome}', não possui o utilitário equipado no inventário.")
        if any(v.nome == vestimenta.nome and v.tipo == TipoItem.VESTIMENTA for v in self.__inventario):
            self.__vestimenta = vestimenta
            print(f"A vestimenta '{vestimenta.nome}' foi equipada em {self.nome}")
            efeitoVida+= vestimenta.valorEfeito
        else:
            print(f"ERROR: o jogador '{self.nome}', não possui a vestimenta equipada no inventário.")
        
        self.__vida = self.vidaBase + (efeitoVida/100)*self.vidaBase
        if self.__vida > 100:
            self.__vida = 100
        self.__ataqueBase = self.ataque + efeitoDano
        
    def add_Item(self, item):
        if not any(i.nome == item.nome for i in self.__inventario):
            self.__inventario.append(item)
            print(f"O item '{item.nome}' foi adicionado ao inventário de {self.nome}")
        else:
            print(f"O item '{item.nome}', já está no inventário de {self.nome}.")

    def remove_Item(self, item):
        if not any(i.nome == item.nome for i in self.__inventario):
            print(f"O item '{item.nome}', não se encontra no inventário de {self.nome}")
            return

        self.__inventario.remove(item)

        # Des-equipar de forma segura (evita crash quando equipamento não está definido)
        if self.__arma is not None and self.__arma.nome == item.nome and self.__arma.tipo == TipoItem.ARMA:
            self.__arma = None

        if self.__vestimenta is not None and self.__vestimenta.nome == item.nome and self.__vestimenta.tipo == TipoItem.VESTIMENTA:
            self.__vestimenta = None

        if self.__utilitario is not None and self.__utilitario.nome == item.nome and self.__utilitario.tipo == TipoItem.UTILITARIO:
            self.__utilitario = None

        print(f"O item '{item.nome}', foi removido do inventário de {self.nome}")


    def mostrar_Inventario(self):
        for i in self.__inventario:
            print(f"-> {i.nome}  |  {i.valorEfeito}  |  {i.descricao}  |  {i.tipo.value}")

