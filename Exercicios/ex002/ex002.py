#declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade
    para criar uma nova pessoa use:
    variável = Gafanhoto("Nome",idade)
    """
    def __init__(self,nome="Vazio",idade=0): 
        self.nome = nome # todo atributo tem um self ma frente,ex: self.nome e não tem parenteses
        self.idade = idade

    # Métodos de instância
    def aniversario(self):
        self.idade = self.idade +1 

    def __str__(self): # Dunder Method, é um metodo que mostra os dados do objetos --> print(g1)
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"
    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"
#declaração de Objeto    
g1 = Gafanhoto("Arthur",16) 
print(g1)
print(g1.__dict__) # Dunder Attribute
print(g1.__getstate__()) # Dunder Method,pode ser personalizado na criação da classe
print(g1.__class__) # Dunder Attribute
#print(Gafanhoto.__doc__) # Dunder Attribute