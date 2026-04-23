from tipo_item import ItemTipo

class Item:
    def __init__ (self, nome, descricao, atributo, tipo = ""):
        self.nome = nome
        self.descricao = descricao
        self.atributo = atributo
        self.tipo = tipo

    @property
    def nome(self):
        return self.__nome
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def atributo(self):
        return self.__atributo
    
    @property
    def tipo(self):
        return self.__tipo

    def __str__ (self):
        return f"------ Item ------\nNome: {self.__nome}\nDescrição: {self.atributo}\nTipo: {self.tipo}\n"
    
    def __eq__(self, outro):
        if not isinstance(outro, Item):
            return False
        return self.nome == outro.nome and self.descricao == outro.descricao