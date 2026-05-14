from tipo_item import TipoItem

class Item:
    def __init__ (self, nome, descricao, valorEfeito: float, tipo: TipoItem):
        self.__nome = nome
        self.__descricao = descricao
        self.__valorEfeito = valorEfeito
        self.__tipo = tipo

    @property
    def nome(self):
        return self.__nome
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def valorEfeito(self):
        return self.__valorEfeito
    
    @property
    def tipo(self):
        return self.__tipo

    def __str__ (self):
        return f"------ Item ------\nNome: {self.__nome}\nDescrição: {self.__descricao}\nValor do efeito: {self.__valorEfeito}\nTipo: {self.__tipo.value}\n"
    
    def __eq__(self, outro):
        if not isinstance(outro, Item):
            return False
        return self.__nome == outro.nome and self.__descricao == outro.descricao and self.__tipo == outro.tipo